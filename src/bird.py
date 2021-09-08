import re
from ast import literal_eval as le
import threading
import random
gvar = {'using': {'type': 'funct', 'dt': {'attrib': {'file': ['', '']}, 'code': "\n\tcreate var libdir array_item(dirsarray,'lib');\n\tcreate var packagedir array_item(dirsarray,'package');\n\tpyparse `try:\n\tparse(open('@{file}').read())\nexcept FileNotFoundError:\n\ttry:\n\t\tparse(open('@{libdir}@{file}').read())\n\texcept FileNotFoundError:\n\t\tparse(open('@{packagedir}/@{file}/main.bd').read())`\n", 'head': {'sep': '-', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}}, 'typeof': {'type': 'funct', 'dt': {'attrib': {'item': ['', '']}, 'code': '\n\tpyparse `var["data"] = {\'type\':\'string\',\'dt\':var[\'item\'][\'type\']}`;\n\treturn data\n', 'head': {'global': '', 'sep': '~'}}}, 'dirsarray': {'dt': {'bird': {'type': 'string', 'dt': 'Bird/'}, 'lib': {'type': 'string', 'dt': 'Bird/lib/'}, 'package': {'type': 'string', 'dt': 'Bird/package'}}, 'type': 'associative'}, 'array_item': {'type': 'funct', 'dt': {'attrib': {'arr': ['', ''], 'cnt': ['', '']}, 'code': "\n\tcreate var data 'notdefined';\n\tpyparse `if var['cnt']['type'] == 'number':\n\tvar['cnt']['dt'] = int(var['cnt']['dt'])\nvar['data']['dt'] = var['arr']['dt'][var['cnt']['dt']]['dt']`;\n\treturn data\n", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}}, 'eval': {'type': 'funct', 'dt': {'attrib': {'code': ['', '']}, 'code': "pyparse `parse('''@{code}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}, 'quit': {'type': 'funct', 'dt': {'attrib': {'status': ['number', 0.0]}, 'code': 'pyparse `quit(int(@{status}))`', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}}
var = {}
classes = {}
def null(*args):
	pass
d = {'cnt':0,'ep':'','retd':'','break':False,'funct':False,'run':True,'els':False,'lastif':0,'interval':{},'class':'','atc':null,'ecnt':0,'atcd':'','atcdat':[]}
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
		for item in re.findall(r'@\{([^}]*)\}',txt,re.DOTALL):
			if re.match(r'^[ +\t\n]*([a-zA-Z_]+[^@|.\n\t (]*)[ +\t\n]*$',item):
				dat = re.match(r'^[ +\t\n]*([a-zA-Z_]+[^@|\n\t (]*)[ +\t\n]*$',item)
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
	elif re.match(r'^[ \t\n]*([a-zA-Z_]+[^@|\n\t ]*)\((.*)\)[ \t\n]*$',txt):
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
	elif re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL):
		dt = re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL)
		dt = re.split(r'[ +\t\n]*[&+][ +\t\n]*',dt[1])
		l = {}
		for item in dt:
			dat = re.match('(.*)[:$](.*)',item,re.DOTALL)
			l[typeify(dat[1])[1]] = {'type':typeify(dat[2])[0],'dt':typeify(dat[2])[1]}
		txt = l
		ty = 'associative'
	elif re.match(r'[ \t\n+]*funct[ \t\n+]*\((.*)\)\{(.*)\}[ +\t\n]*(\[.*\]){0,1}',txt,re.DOTALL):
		it = shfunct(re.match(r'[ \t\n+]*funct[ \t\n+]*\((.*)\)\{(.*)\}[ +\t\n]*(\[.*\]){0,1}',txt,re.DOTALL))
		txt = it['dt']
		ty = it['type']
	elif re.match(r'[ \t\n+]*(true|false|B1|B0)[ \t\n+]*',txt):
		dt = re.match(r'[ \t\n+]*(true|false|B1|B0)[ \t\n+]*',txt)
		ty = 'bool'
		if dt[1] == 'true' or dt[1] == 'B1':
			txt = 'True'
		else:
			txt = 'False'
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
	n = regex[2]
	if d['class'] != "":
		n = d['class']+n
	if regex[1]:
		for item in regex[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	txt = regex[3]
	typ = typeify(txt)
	var[n] = {}
	var[n]['dt'] = typ[1]
	var[n]['type'] = typ[0]
	if 'global' in head.keys():
		gvar[n] = {}
		gvar[n]['dt'] = typ[1]
		gvar[n]['type'] = typ[0]
def fatc(dt='',regex=[],tr=''): #Function ATC
	if dt != '':
		tr = re.match(r'[ +\t\n]*}[ +\t\n]*(\[.*\]){0,1}',tr)
		head = {'sep':':','scb':'\\scb','ecb':'\\ecb'}
		n = regex[1]
		if tr[1]:
			for item in tr[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
				item = item.split('=')
				head[item[0]] = item[1]
		var[n]['dt'] = {'attrib':regex[2],'code':dt,'head':head}
		if 'global' in head.keys():
			gvar[n] = {'dt':{'attrib':regex[2],'code':dt,'head':head},'type':'funct'}
	else:
		return 'a'
def cfunct(regex):
	n = regex[1]
	if d['class'] != "":
		n = d['class']+n
		if var[d['class'][::-1].replace('.','',1)[::-1]]['dt'] == f"<class {d['class'][::-1].replace('.','',1)[::-1]} instance class>":
			if regex[1] == 'construct':
				n = d['class'][::-1].replace('.','',1)[::-1]
	var[n] = {}
	var[n]['type'] = 'funct'
	head = {'sep':':','scb':'\\scb','ecb':'\\ecb'}
	args = {}
	re2 = regex[2].replace('\\,','\\comma')
	for item in regex[2].split(','):
		item.replace('\\comma',',')
		if len(item.split('=')) == 2:
			args[item.split('=')[0]] = typeify(item.split('=')[1])
		else:
			args[item.split('=')[0]] = ['','']
	d['ecnt'] += 1
	d['atc'] = fatc
	d['atcdat'] = ['',n,args]
	'''var[regex[1]]['dt'] = {'attrib':args,'code':value,'head':head}
	if 'global' in head.keys():
		gvar[regex[1]] = {}
		gvar[regex[1]]['dt'] = {'attrib':args,'code':value,'head':head}
		gvar[regex[1]]['type'] = 'funct'''
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
def ifatc(dt='',data=[],tr=''):
	if dt != '':
		d['atcd'] = ''
		d['atc'] = null
		d['atcdat'] = []
		if eval(typeify(data[0],True)[1]):
			parse(dt)
			d['lastif'] = d['cnt']+1
		else:
			d['els'] = True
	else:
		return 'a'
def ifstate(regex):
	if d['lastif'] == d['cnt'] and re.match(r'else[ +]if',regex[1]):
		d['lastif'] = 0
		return 0
	d['ecnt'] = 1
	d['atcdat'] = [regex[2]]
	d['atc'] = ifatc
def elsatc(value='',dt=[],tr=''):
	if d['els']:
		parse(value)
def els(regex):
	d['ecnt'] = 1
	d['atcdat'] = ''
	d['atc'] = elsatc
def featc(value='',dt=[],tr=''):
	if dt != '':
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
					var[dt[1]] = {'type':'string','dt':i}
					parse(value)
		else:
			v = typeify(dt[3])
			if v[0] == 'associative':
				for i in v[1].keys():
					var[dt[1]] = {'type':'string','dt':i}
					parse(value)
	else:
		return 'a'
def foreach(regex):
	dt = re.match(r'([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]+(in|of)[ +\n\t]+(.*)',regex[1])
	d['ecnt'] = 1
	d['atcdat'] = dt
	d['atc'] = featc
def whatc(value='',regex=[],tr=''):
	while eval(typeify(regex[1])[1]):
		parse(value)
def whileloop(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = whatc
def whenatc(value='',regex=[],tr=''):
	#l = ['',regex[1],value,head]
	l = ['',regex[1],value]
	def when_wrapper(reg):
		if eval(typeify(reg[1])[1]):
			parse(reg[2])
			return 'end'
	set_interval(when_wrapper,0,l)
def when(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = whenatc
def shfunct(regex):
	it = {'type':'funct','dt':{}}
	head = {}
	if regex[3]:
		for item in regex[3].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	value = regex[2]
	if not 'sep' in head.keys():
		head['sep'] = ':'
	value = value.replace('\\'+head['sep'],'\\@seper|')
	value = re.sub(head['sep'],';',value)
	value = value.replace('\\@seper|',head['sep'])
	args = {}
	re2 = regex[1].replace('\\,','\\comma')
	for item in regex[1].split(','):
		item.replace('\\comma',',')
		if len(item.split('=')) == 2:
			args[item.split('=')[0]] = typeify(item.split('=')[1])
		else:
			args[item.split('=')[0]] = ['','']
	it['dt'] = {'attrib':args,'code':value,'head':head}
	return it
def claatc(code='',data=[],tr=''):
	if tr != "":
		tr = re.match(r'[ +\t\n]*}[ +\t\n]*(\[.*\]){0,1}',tr)
		head = {'sep':':','scb':'\\scb','ecb':'\\ecb'}
		if tr[1]:
			for item in tr[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
				item = item.split('=')
				head[item[0]] = item[1]
		typ = data[2]
		if typ == 'instance':
			var[data[1]] = {'type':'class','dt':f'<class {data[1]} instance class>'}
		else:
			var[data[1]] = {'type':'class','dt':f'<class {data[1]} static class>'}
		ocls = d['class']
		d['class'] = data[1]+'.'
		parse(code)
		d['class'] = ocls
	else:
		return 'a'
def cla(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = claatc
cl = {r'''[ +\t\n]*create[ +\t\n]+var(\[.*\]){0,1}[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)(.*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)[ +\t\n]*':[pyparse,'Pyparse'],r'[ +\t\n]*([a-zA-Z_]+[^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*':[callfunct,'Call Function'],r'[ +\t\n]*return[ +\t\n]*([^\n]*)':[RETURN,'Return'],r'[ +\t\n]*(if|else[ +]if)[ +\t\n]*\((.*)\)[ +\t\n]*\{':[ifstate,'If Statement'],r'[ +\t\n]*else[ +\t\n]*\{':[els,'Else'],r'[ +\t\n]*foreach[ +\t\n]*\((.*)\)[ +\t\n]*\{':[foreach,'Foreach Loop'],r'[ +\t\n]*while[ +\t\n]*\((.*)\)[ +\t\n]*\{':[whileloop,'While Loop'],r'[ +\t\n]*when[ +\t\n]*\((.*)\)[ +\t\n]*\{':[when,'When Loop'],"":[null,'WhiteSpace'],r"[ +\t\n]*create[ +\t\n]+class[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\([ +\t\n]*(instance|static)[ +\t\n]*\)[ +\t\n]*\{":[cla,'Class']}
def parse(code):
	code = code.replace('\\;','\\semi')
	code = re.sub(r'//[^/]*//','',code)
	code = re.sub(r'\)[ +\t\n]*\{','){;',code)
	code = re.sub(r'else[ +\t\n]*\{','else{;',code)
	if re.match(r';[ +\t\n]*$',code):
		code = re.sub(r';[ +\t\n]*$','',code)
	nels = False
	for line in re.split(r';[\n \t+]*',code):
		if d['ecnt'] == 0:
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
		else:
			d['ep'] = line
			d['cnt'] += 1
			line = line.replace('\\semi',';')
			for sb in re.findall(r'{',line):
				d['ecnt'] += 1
			for eb in re.findall(r'}',line):
				d['ecnt'] -= 1
			if d['ecnt'] == 0:
				d['atc'](d['atcd'][::-1].replace(';','',1)[::-1],d['atcdat'],line)
				d['atcd'] = ''
				d['atc'] = null
				d['atcdat'] = []
			else:
				d['atcd'] += line+';'