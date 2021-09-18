import re
from ast import literal_eval as le
import threading
import random
import base64
from pathlib import Path
import os
home = str(Path.home())+'/Bird-Lang' #Only for Replit: +'/Bird-Lang'
bddir = open(home+'/bddir.txt').read()
gvar = {'using': {'dt': {'attrib': {'file': ['', ''], 'global': ['bool', 'True']}, 'code': "create var libdir array_item(dirsarray,'lib');create var packagedir array_item(dirsarray,'package');if (global){;if(exists usingpasswd){;create var passwd B1;};else{;create var passwd B0;};pyparse `try:\n\tif '''@{@fn}''' == '''@{file}''':\n\t\traise FileNotFoundError('')\n\telse:\n\t\topen('@{file}')\n\t\tparse(open('@{file}').read())\nexcept FileNotFoundError:\n\ttry:\n\t\topen('@{libdir}@{file}')\n\t\tparse(open('@{libdir}@{file}').read())\n\texcept FileNotFoundError:\n\t\ttry:\n\t\t\topen('@{packagedir}/@{file}/passwd.txt')\n\t\t\tif eval(var['passwd']['dt']):\n\t\t\t\tpasswd = base64.b64decode(open('@{packagedir}/@{file}/passwd.txt').read()).decode('utf-8')\n\t\t\t\tif var['usingpasswd']['dt'] == passwd:\n\t\t\t\t\tparse(open('@{packagedir}/@{file}/main.bd').read())\n\t\texcept:\n\t\t\tparse(open('@{packagedir}@{file}/main.bd').read())`;};else{;if(exists usingpasswd){;create var passwd B1;};else{;create var passwd B0;};create class dt(static){;pyparse `try:\n\tif '''@{@fn}''' == '''@{file}''':\n\t\traise FileNotFoundError('')\n\telse:\n\t\topen('@{file}')\n\t\tparse(open('@{file}').read())\nexcept FileNotFoundError:\n\ttry:\n\t\topen('@{libdir}@{file}')\n\t\tparse(open('@{libdir}@{file}').read())\n\texcept FileNotFoundError:\n\t\ttry:\n\t\t\topen('@{packagedir}/@{file}/passwd.txt')\n\t\t\tif eval(var['passwd']['dt']):\n\t\t\t\tpasswd = base64.b64decode(open('@{packagedir}/@{file}/passwd.txt').read()).decode('utf-8')\n\t\t\t\tif var['usingpasswd']['dt'] == passwd:\n\t\t\t\t\tparse(open('@{packagedir}/@{file}/main.bd').read())\n\t\texcept:\n\t\t\tparse(open('@{packagedir}@{file}/main.bd').read())`;};return dt;}", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}, 'type': 'funct'}, 'typeof': {'type': 'funct', 'dt': {'attrib': {'item': ['', '']}, 'code': '\n\tpyparse `var["data"] = {\'type\':\'string\',\'dt\':var[\'item\'][\'type\']}`;\n\treturn data\n', 'head': {'global': '', 'sep': '~'}}}, 'array_item': {'type': 'funct', 'dt': {'attrib': {'arr': ['', ''], 'cnt': ['', '']}, 'code': "\n\tcreate var data 'notdefined';\n\tpyparse `if var['cnt']['type'] == 'number':\n\tvar['cnt']['dt'] = int(var['cnt']['dt'])\nvar['data']['dt'] = var['arr']['dt'][var['cnt']['dt']]['dt']`;\n\treturn data\n", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}}, 'eval': {'type': 'funct', 'dt': {'attrib': {'code': ['', '']}, 'code': "pyparse `parse('''@{code}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}, 'quit': {'type': 'funct', 'dt': {'attrib': {'status': ['number', 0.0]}, 'code': 'pyparse `quit(int(@{status}))`', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}, 'dirsarray': {'dt': {'bird': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/'}, 'lib': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/lib/'}, 'package': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/package/'}}, 'type': 'associative'}, 'fread': {'dt': {'attrib': {'fn': ['', '']}, 'code': 'pyparse `var[\'data\'] = {\'type\':\'string\',\'dt\':open("@{fn}").read()}`;return data', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}, 'type': 'funct'}, 'fwrite': {'dt': {'attrib': {'fn': ['', ''], 'txt': ['', ''], 'm': ['string', 'a']}, 'code': "pyparse `d = open('''@{fn}''','''@{m}''')\nd.write('''@{txt}''')\nd.close()`;return true", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}, 'type': 'funct'}, 'fdelete': {'dt': {'attrib': {'fn': ['', '']}, 'code': "pyparse `import os\nos.remove('''@{fn}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': ''}}, 'type': 'funct'}}
gvar['dirsarray'] = {'dt': {'bird': {'type': 'string', 'dt': bddir+'/'}, 'lib': {'type': 'string', 'dt': f'{bddir}/lib/'}, 'package': {'type': 'string', 'dt': f'{bddir}/package/'}}, 'type': 'associative'}
var = {}
classes = {}
def null(*args,**kwargs):
	pass
d = {'cnt':0,'ep':'','retd':'','break':False,'funct':False,'run':True,'els':False,'lastif':0,'interval':{},'class':'','atc':null,'ecnt':0,'atcd':'','atcdat':[],'lt':0,'errh':{},'clsd':{}}
def error(n,t):
	try:
		parse(d['errh'][n])
	except:
		try:
			parse(d['errh']['Error'])
		except:
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
def typeify(txt,qt=False,err=True):
	txt = re.match(r'^[ +\n\t]*(.*)[ +\n\t]*$',txt,re.DOTALL)[1]
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
			if re.match(r'^[ +\t\n]*([a-zA-Z_@]+[^|\n\t (]*)[ +\t\n]*$',item):
				dat = re.match(r'^[ +\t\n]*([a-zA-Z_@]+[^|\n\t (]*)[ +\t\n]*$',item)
				if '.' in dat[1]:
					n = dat[1].split('.')
					data = var
					cnt = 1
					for i in n:
						if cnt == len(n):
							data = data[i]['dt']
						else:
							if data[i]['type'] == 'class':
								data = data[i]['dt']
						cnt += 1
					if qt:
						txt = txt.replace(f'@{{{dat[1]}}}','"'+data+'"')
					else:
						txt = txt.replace(f'@{{{dat[1]}}}',data)
				else:
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
	elif re.match(r'^[ \t\n]*([a-zA-Z_]+[^|\n\t ]*)\((.*)\)[ \t\n]*$',txt):
		oretd = d['retd']
		d['retd'] = '@keycode42125256strexec|'
		parse(txt)
		ret = d['retd']
		d['retd'] = oretd
		return ret
	elif re.match(r'[ +\t\n]*exists[ +\t\n]+(.*)[ +\t\n]*',txt):
		if typeify(re.match(r'[ +\t\n]*exists[ +\t\n]+(.*)[ +\t\n]*',txt)[1],err=False) == 'VE,UV':
			return ['bool','False']
		else:
			return ['bool','True']
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
	elif re.match(r'^[ \t\n+]*create[ \t\n+]+([a-zA-Z_]+[^@|\n\t (]*)[ \t\n+]*\((.*)\)',txt,re.DOTALL):
		dat = re.match(r'^[ \t\n+]*create[ \t\n+]+([a-zA-Z_]+[^@|\n\t (]*)[ \t\n+]*\((.*)\)',txt,re.DOTALL)
		n = dat[1]
		arg = dat[2]
		dt = var[n]
		var[n]['dt'] = le(base64.b64decode(var[n]['dt']).decode('utf-8'))
		parse(f'{n}.initiate({arg});')
		ty = 'class'
		txt = var[n]['dt']
		var[n] = dt
	elif re.match(r'[ \t\n+]*(true|false|B1|B0)[ \t\n+]*',txt):
		dt = re.match(r'[ \t\n+]*(true|false|B1|B0)[ \t\n+]*',txt)
		ty = 'bool'
		if dt[1] == 'true' or dt[1] == 'B1':
			txt = 'True'
		else:
			txt = 'False'
	else:
		if '.' in txt:
			n = txt.split('.')
			dat = var
			cnt = 1
			for i in n:
				if cnt == len(n):
					ty = dat[i]['type']
					txt = dat[i]['dt']
				else:
					if dat[i]['type'] == 'class':
						dat = dat[i]['dt']
				cnt += 1
		else:
			if txt in var.keys():
				ty = var[txt]['type']
				txt = var[txt]['dt']
			elif txt in gvar.keys():
				ty = gvar[txt]['type']
				txt = gvar[txt]['dt']
			else:
				if err:
					error('VarError',f'Unknown Var "{txt}".')
				else:
					return 'VE,UV'
	return [ty,txt]
def cvar(regex):
	head = {}
	n = regex[2]
	'''if d['class'] != "":
		n = d['class']+n'''
	if regex[1]:
		for item in regex[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	txt = regex[3]
	typ = typeify(txt)
	if d['class'] == '':
		var[n] = {}
		var[n]['dt'] = typ[1]
		var[n]['type'] = typ[0]
		if 'global' in head.keys():
			gvar[n] = {}
			gvar[n]['dt'] = typ[1]
			gvar[n]['type'] = typ[0]
	else:
		n = txt.split('.')
		dat = var
		cnt = 1
		data = {}
		for i in n:
			if cnt == len(n):
				ty = dat[i]['type']
				txt = dat[i]['dt']
			else:
				if dat[i]['type'] == 'class':
					dat = dat[i]['dt']
			#data[i] = 
			cnt += 1
		
def fatc(dt='',regex=[],tr=''): #Function ATC
	if dt != '':
		tr = re.match(r'[ +\t\n]*}[ +\t\n]*(\[.*\]){0,1}',tr)
		head = {'sep':':','scb':'\\scb','ecb':'\\ecb'}
		n = regex[1]
		if tr[1]:
			for item in tr[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
				item = item.split('=')
				head[item[0]] = item[1]
		if d['class'] == '':
			var[n]['dt'] = {'attrib':regex[2],'code':dt,'head':head}
			if 'global' in head.keys():
				gvar[n] = {'dt':{'attrib':regex[2],'code':dt,'head':head},'type':'funct'}
		else:
			d['clsd'][d['class']][n] = {'type':'funct','dt':{'attrib':regex[2],'code':dt,'head':head}}
	else:
		return 'a'
def cfunct(regex):
	n = regex[1]
	'''if d['class'] != "":
		n = d['class']+n
		if var[d['class'][::-1].replace('.','',1)[::-1]]['dt'] == f"<class {d['class'][::-1].replace('.','',1)[::-1]} instance class>":
			if regex[1] == 'construct':
				n = d['class'][::-1].replace('.','',1)[::-1]'''
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
	if '.' in fn:
		txt = fn
		n = txt.split('.')
		dat = var
		cnt = 1
		for i in n:
			if cnt == len(n):
				dat = dat[i]
			else:
				if dat[i]['type'] == 'class':
					dat = dat[i]['dt']
			cnt += 1
	else:
		dat = var[fn]
	if not dat['type'] == 'funct':
		#error
		pass
	for i,n in dat['dt'].items():
		dat[i] = n
	att = {}
	for i,n in dat['dt']['attrib'].items():
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
	dt = re.match(r'([a-zA-Z_]+[^|.\n\t ]*)[ +\n\t]+(in|of)[ +\n\t]+(.*)',regex[1])
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
		d['clsd'][d['class']] = {}
		parse(code)
		if typ == 'static':
			var[data[1]] = {'type':'class','dt':d['clsd'][d['class']]}
		else:
			var[data[1]] = {'type':'class','dt':base64.b64encode(str.encode(str(d['clsd'][d['class']])))}
		del d['clsd'][d['class']]
		d['class'] = ocls
	else:
		return 'a'
def cla(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = claatc
def errhatc(code='',data=[],tr=''):
	d['errh'][data[1]] = code
def errh(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = errhatc
def globalize(regex):
	dat = regex
	if '.' in dat[1]:
		n = dat[1].split('.')
		data = var
		cnt = 1
		for i in n:
			if cnt == len(n):
				data = data[i]
			else:
				if data[i]['type'] == 'class':
					data = data[i]['dt']
			cnt += 1
		gvar[i] = data
	else:
		if dat[1] in var:
			gvar[dat[1]] = var[dat[1]]
		else:
			error('VarError',f'Unknown Var "{dat[1]}".')
cl = {r'''[ +\t\n]*create[ +\t\n]+var(\[.*\]){0,1}[ +\t\n]+([a-zA-Z_]+[^@|\n\t ]*)(.*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)[ +\t\n]*':[pyparse,'Pyparse'],r'[ +\t\n]*([a-zA-Z_]+[^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*':[callfunct,'Call Function'],r'[ +\t\n]*return[ +\t\n]*([^\n]*)':[RETURN,'Return'],r'[ +\t\n]*(if|else[ +]if)[ +\t\n]*\((.*)\)[ +\t\n]*\{':[ifstate,'If Statement'],r'[ +\t\n]*else[ +\t\n]*\{':[els,'Else'],r'[ +\t\n]*foreach[ +\t\n]*\((.*)\)[ +\t\n]*\{':[foreach,'Foreach Loop'],r'[ +\t\n]*while[ +\t\n]*\((.*)\)[ +\t\n]*\{':[whileloop,'While Loop'],r'[ +\t\n]*when[ +\t\n]*\((.*)\)[ +\t\n]*\{':[when,'When Loop'],"":[null,'WhiteSpace'],r"[ +\t\n]*create[ +\t\n]+class[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\([ +\t\n]*(instance|static)[ +\t\n]*\)[ +\t\n]*\{":[cla,'Class'],r'[ +\t\n]*create ErrorHandler[ +\t\n]*\((.*)\)[ +\t\n]*\{':[errh,"Create Error Handler"],r'[ +\t\n]*global[ +\t\n]*(.*)[ +\t\n]*':[globalize,'Global']}
def parse(code):
	code = code.replace('\\;','\\semi')
	code = re.sub(r'//(.*)*//','',code,re.DOTALL)
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