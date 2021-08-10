import re
from ast import literal_eval as le
d = {'cnt':0}
def error(n,t):
	print(f'{n} triggered on line {str(d["cnt"])}: {t}')
	quit(1)
def typeify(txt):
	if txt.startswith('"') and txt.endswith('"'):
		ty = 'string'
		txt = txt.replace('"','')
	elif txt.startswith("'") and txt.endswith("'"):
		ty = 'string'
		txt = txt.replace("'",'')
	elif re.match(r"^[0-9.]*$",txt):
		txt = float(txt)
		ty = 'number'
	return [ty,txt]
def cvar(regex):
	txt = regex[2]
	var[regex[1]] = {}
	typ = typeify(txt)
	var[regex[1]]['dt'] = typ[1]
	var[regex[1]]['type'] = typ[0]
def cfunct(regex):
	var[regex[1]] = {}
	var[regex[1]]['type'] = 'funct'
	head = {}
	if regex[4]:
		for item in regex[4].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	value = regex[3]
	if not 'sep' in head.keys():
		head['sep'] = ':'
	value = re.sub(head['sep'],';',value)
	args = {}
	for item in regex[2].split(','):
		if len(item.split('=')) == 2:
			args[item.split('=')[0]] = typeify(item.split('=')[1])
		else:
			args[item.split('=')[0]] = ['','']
	var[regex[1]]['dt'] = {'attrib':args,'code':value,'head':head}
def null(regex):
	pass
def pyparse(regex):
	exec(regex[1])
cl = {r'''[ +\t\n]*create[ +\t\n]+var[ +\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t]+([^\n]*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{([^;]*)\}[ +\t\n]*(\[.*\]){0,1}':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)':[pyparse,'Pyparse'],r'[ +\t\n]*([a-zA-Z_]+[^@|.\n\t ]*)\((.*)\)'}
var = {}
def parse(code):
	code = code.replace('\\;','\\semi')
	for line in re.split(r';[\n \t]*',code):
		d['cnt'] += 1
		line = line.replace('\\semi',';')
		fnd = False
		for reg,funct in cl.items():
			if re.match('^'+reg+'$',line):
				funct[0](re.match('^'+reg+'$',line))
				fnd = True
				break
		if not fnd:
			error('SyntaxError',f'No Such Command, {line}.')
