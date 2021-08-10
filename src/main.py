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
	value.replace(head['sep'],';')
	var[regex[1]]['dt'] = {'attrib':le('('+regex[2]+')'),'code':value,'head':head}
def null(regex):
	pass
def pyparse(regex):
	exec(regex[1])
cl = {r'''create[ +\t]+var[ +\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t]+([^\n]*)''':[cvar,'Create Var'],r'create[ +\t]+funct[ +\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t]*\((.*)\)[ +\t]*\{(.*)\}(\[.*\]){0,1}':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'pyparse[ +\t]+(.*)':[pyparse,'Pyparse']}
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
parse(open('test.bd').read())
