import re
from ast import literal_eval as le
import threading
import random
gvar = {'using': {'type': 'funct', 'dt': {'attrib': {'file': ['', '']}, 'code': "\n\tpyparse `try:\n\tparse(open('@{file}').read())\nexcept FileNotFoundError:\n\tparse(open('Bird/lib/@{file}').read())`\n", 'head': {'global': '', 'sep': '-'}}}, 'typeof': {'type': 'funct', 'dt': {'attrib': {'item': ['', '']}, 'code': '\n\tpyparse `var["data"] = {\'type\':\'string\',\'dt\':var[\'item\'][\'type\']}`;\n\treturn data\n', 'head': {'global': '', 'sep': '~'}}}}
var = {}
d = {'cnt':0,'ep':'','retd':'','break':False,'funct':False,'run':True,'els':False,'lastif':0,'interval':{}}
def error(n,t):
	print(f'{n} triggered at expression {str(d["cnt"])}, "{d["ep"]}": {t}')
	quit(1)
def set_interval(func,sec=0,reg=[]):
    idnt = random.randint(0,9999999999)
    def func_wrapper():
        if func(reg) == 'end':
            return ''
        set_interval(func, sec,reg)
    t = threading.Timer(sec,func_wrapper)
    t.start()
    d['interval'][idnt] = t
    return idnt
def typeify(txt,qt=False):
	if txt.startswith('"') and txt.endswith('"'):
		ty = 'string'
		txt = txt.replace('"','')
		return [ty,txt]
	elif re.match(r"^[ +\n\t]*'(.*)'[ +\n\t]*",txt,re.DOTALL):
		ty = 'string'
		txt = re.sub(r"^[ +\n\t]*'",'',txt,1)
		txt = re.sub(r"'[ +\n\t]*$",'',txt,1)
		return [ty,txt]
	elif re.match(r"^[ +\n\t]*`(.*)`[ +\n\t]*$",txt,re.DOTALL):
		ty = 'string'
		txt = re.sub(r"^[ +\n\t]*`",'',txt,1)
		txt = re.sub(r"`[ +\n\t]*$",'',txt,1)
		'''for n,v in var.items():
			if not v['type'] == 'funct':
				#error('FormattedStringError','Cannot insert type "funct" into formatted string.')
				txt = txt.replace('\\@','@|').replace('@{'+n+'}',str(v['dt'])).replace('@|','@')
		for n,v in gvar.items():
			if not v['type'] == 'funct':
				txt = txt.replace('\\@','@|').replace('@{'+n+'}',str(v['dt'])).replace('@|','@')'''
		for item in re.findall(r'@\{([^}]*)\}',txt,re.DOTALL):
			if re.match(r'^[ +\t\n]*([a-zA-Z_]+[^@|.\n\t (]*)[ +\t\n]*$',item):
				dat = re.match(r'^[ +\t\n]*([a-zA-Z_]+[^@|.\n\t (]*)[ +\t\n]*$',item)
				if dat[1] in var:
					if var[dat[1]]['type'] == 'funct':
						pass
					else:
						if qt:
							txt = txt.replace(f'@{{{dat[1]}}}','"'+str(var[dat[1]]['dt'])+'"')
						else:
							txt = txt.replace(f'@{{{dat[1]}}}',str(var[dat[1]]['dt']))
				else:
					error('VarError',f'Unknown Var "{dat[1]}".')
			else:
				oret = d['retd']
				parse(item)
				if qt:
					txt = txt.replace(f'@{{{item}}}','"'+str(d["retd"][1])+'"')
				else:
					txt = txt.replace(f'@{{{item}}}',str(d["retd"][1]))
				d['retd'] = oret
		return [ty,txt]
	elif re.match(r"^[0-9.]+$",txt):
		txt = float(txt)
		ty = 'number'
		return [ty,txt]
	elif re.match(r'^[ \t\n]*$',txt):
		ty = 'null'
		txt = ''
		return [ty,txt]
	elif re.match(r'^[ \t\n]*([a-zA-Z_]+[^@|.\n\t ]*)\((.*)\)[ \t\n]*$',txt):
		oretd = d['retd']
		d['retd'] = '@keycode42125256strexec|'
		parse(txt)
		ret = d['retd']
		d['retd'] = oretd
		return ret
	elif re.match(r'^[ +\t\n]*(\[.*\])[ +\t\n]*$',txt,re.DOTALL):
		it = re.match(r'^[ +\t\n]*(\[.*\])[ +\t\n]*$',txt,re.DOTALL)[1]
		it = it.replace('\\,','\\comma')
		l = []
		for item in re.match(r'^[ +\t\n]*\[(.*)\][ +\t\n]*$',txt,re.DOTALL)[1].split(','):
			item = item.replace('\\comma',',')
			l.append({'type':typeify(item)[0],'dt':typeify(item)[1]})
		txt = l
		ty = 'array'
	else:
		if txt in var.keys():
			ty = var[txt]['type']
			txt = var[txt]['dt']
		elif txt in gvar.keys():
			ty = gvar[txt]['type']
			txt = gvar[txt]['dt']
		else:
			error('VarError',f'Unknown Var "{txt}".')
	return [ty,txt]
def cvar(regex):
	head = {}
	if regex[1]:
		for item in regex[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	txt = regex[3]
	typ = typeify(txt)
	var[regex[2]] = {}
	var[regex[2]]['dt'] = typ[1]
	var[regex[2]]['type'] = typ[0]
	if 'global' in head.keys():
		gvar[regex[2]] = {}
		gvar[regex[2]]['dt'] = typ[1]
		gvar[regex[2]]['type'] = typ[0]
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
	value = value.replace('\\'+head['sep'],'\\@seper|')
	value = re.sub(head['sep'],';',value)
	value = value.replace('\\@seper|',head['sep'])
	args = {}
	re2 = regex[2].replace('\\,','\\comma')
	for item in regex[2].split(','):
		item.replace('\\comma',',')
		if len(item.split('=')) == 2:
			args[item.split('=')[0]] = typeify(item.split('=')[1])
		else:
			args[item.split('=')[0]] = ['','']
	var[regex[1]]['dt'] = {'attrib':args,'code':value,'head':head}
	if 'global' in head.keys():
		gvar[regex[1]] = {}
		gvar[regex[1]]['dt'] = {'attrib':args,'code':value,'head':head}
		gvar[regex[1]]['type'] = 'funct'
def null(regex):
	pass
def pyparse(regex):
	exec(typeify(regex[1])[1])
def callfunct(regex):
	global var
	fn = regex[1]
	args = regex[2]
	if not var[fn]['type'] == 'funct':
		#error
		pass
	dat = {}
	for i,n in var[fn]['dt'].items():
		dat[i] = n
	att = {}
	for i,n in var[fn]['dt']['attrib'].items():
		att[i] = n
	cnt = 0
	nvar = gvar
	attl = []
	args = args.replace('\\,','\\comma')
	for item in args.split(','):
		item = item.replace('\\comma',',')
		item = typeify(item)
		attl.append(item)
	for i,n in att.items():
		try:
			attl[cnt]
		except IndexError:
			break
		nvar[i] = {'type':attl[cnt][0],'dt':attl[cnt][1]}
		cnt += 1
	ncnt = 0
	for item,v in dat['attrib'].items():
		if ncnt >= cnt:
			if v != ['','']:
				nvar[item] = {'type':v[0],'dt':v[1]}
		ncnt += 1
	d['funct'] = True
	ov = var
	var = nvar
	parse(dat['code'])
	d['funct'] = False
	var = ov
def RETURN(regex):
	d['retd'] = typeify(regex[1])
def ifstate(regex):
	if d['lastif'] == d['cnt'] and re.match(r'else[ +]if',regex[1]):
		d['lastif'] = 0
		return 0
	head = {'sep':':'}
	if regex[4]:
		for item in regex[4].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	if eval(typeify(regex[2],True)[1]):
		parse(regex[3].replace(head['sep'],';'))
		d['lastif'] = d['cnt']+1
	else:
		d['els'] = True
def els(regex):
	head = {'sep':':'}
	if regex[2]:
		for item in regex[2].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	if d['els']:
		parse(regex[1].replace(head['sep'],';'))
def foreach(regex):
	head = {'sep':':'}
	if regex[3]:
		for item in regex[3].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	value = regex[2]
	value = value.replace('\\'+head['sep'],'\\@seper|')
	value = re.sub(head['sep'],';',value)
	value = value.replace('\\@seper|',head['sep'])
	dt = re.match(r'([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]+(in|of)[ +\n\t]+(.*)',regex[1])
	if dt[2] == 'in':
		v = typeify(dt[3])
		if v[0] == 'number':
			for n in range(0,int(v[1])):
				var[dt[1]] = {'type':'number','dt':n}
				parse(value)
		elif v[0] == 'array':
			for i in v[1]:
				var[dt[1]] = i
				parse(value)
		else:
			for i in v[1]:
				var[dt[1]] = {'type':'string','dt':n}
				parse(value)
def whileloop(regex):
	head = {'sep':':'}
	if regex[3]:
		for item in regex[3].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	value = regex[2]
	value = value.replace('\\'+head['sep'],'\\@seper|')
	value = re.sub(head['sep'],';',value)
	value = value.replace('\\@seper|',head['sep'])
	while eval(typeify(regex[1])[1]):
		parse(value)
def when(regex):
	head = {'sep':':'}
	if regex[3]:
		for item in regex[3].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	value = regex[2]
	value = value.replace('\\'+head['sep'],'\\@seper|')
	value = re.sub(head['sep'],';',value)
	value = value.replace('\\@seper|',head['sep'])
	l = ['',regex[1],value,head]
	def when_wrapper(reg):
		if eval(typeify(reg[1])[1]):
			parse(reg[2])
			return 'end'
	set_interval(when_wrapper,0,l)
cl = {r'''[ +\t\n]*create[ +\t\n]+var(\[.*\]){0,1}[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t]+([^\n]*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{([^;]*)\}[ +\t\n]*(\[.*\]){0,1}':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)':[pyparse,'Pyparse'],r'[ +\t\n]*([a-zA-Z_]+[^@|.\n\t (]*)[ +\t\n]*\((.*)\)':[callfunct,'Call Function'],r'[ +\t\n]*return[ +\t\n]*([^\n]*)':[RETURN,'Return'],r'[ +\t\n]*(if|else[ +]if)[ +\t\n]*\((.*)\)[ +\t\n]*\{(.*)\}[ +\t\n]*(\[.*\]){0,1}':[ifstate,'If Statement'],r'[ +\t\n]*else[ +\t\n]*\{(.*)\}[ +\t\n]*(\[.*\]){0,1}':[els,'Else'],r'[ +\t\n]*foreach[ +\t\n]*\((.*)\)[ +\t\n]*\{(.*)\}[ +\t\n]*(\[.*\]){0,1}':[foreach,'Foreach Loop'],r'[ +\t\n]*while[ +\t\n]*\((.*)\)[ +\t\n]*\{(.*)\}[ +\t\n]*(\[.*\]){0,1}':[whileloop,'While Loop'],r'[ +\t\n]*when[ +\t\n]*\((.*)\)[ +\t\n]*\{(.*)\}[ +\t\n]*(\[.*\]){0,1}':[when,'When Loop']}
def parse(code):
	code = code.replace('\\;','\\semi')
	code = re.sub(r'//[^/]*//','',code)
	nels = False
	for line in re.split(r';[\n \t]*',code):
		if not d['break']:
			if d['run']:
				d['ep'] = line
				d['cnt'] += 1
				line = line.replace('\\semi',';')
				for n,v in gvar.items():
					if not n in var:
						var[n] = v
				fnd = False
				for reg,funct in cl.items():
					if re.match('^'+reg+'$',line,re.DOTALL):
						if funct[1] == 'If Statement':
							nels = True
						if nels and not funct[1] == 'Else':
							d['els'] = False
						dat = funct[0](re.match('^'+reg+'$',line,re.DOTALL))
						fnd = True
						break
				if not fnd:
					error('SyntaxError',f'No Such Command, {line}.')
		else:
			d['break'] = False
			break
