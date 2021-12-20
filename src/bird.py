from os import chdir
import sys
from pathlib import Path
import re
from ast import literal_eval as le
import threading
import random
import argparse
import base64
import os
import urllib3
import json
def ap(text):
	atc = False
	txt = []
	for item in text:
		txt.append(item)
	text = ''
	cnt = 0
	atct = ''
	for char in txt:
		if char == '(' and not atc:
			atct = '('
			atc = True
			text += char
		elif char == ')' and atc:
			atc = False
			text += ')'
		elif char == '[' and not atc:
			atct = '['
			atc = True
			text += char
		elif char == ']' and atc:
			atc = False
			text += char
		elif char == '{' and not atc:
			atct = '{'
			atc = True
			text += char
		elif char == '}' and atc:
			atc = False
			text += char
		elif char == '"':
			if atct == '"' and atc:
				atc = False
				text += char
			elif not atc:
				atc = True
				atct = '"'
				text += char
			else:
				text += char
		elif char == "'":
			if atct == "'" and atc:
				atc = False
				text += char
			elif not atc:
				atc = True
				atct = "'"
				text += char
			else:
				text += char
		elif char == "`":
			if atct == "`" and atc:
				atc = False
				text += char
			elif not atc:
				atc = True
				atct = "`"
				text += char
			else:
				text += char
		elif char == ',' and atc:
			text += '\\c'
		else:
			text += char
		cnt += 1
	return text
def su(home=str(Path.home())):
	global bddir
	global temp
	global gvar
	global opt
	global var
	global classes
	global d
	global typedef
	bddir = open(home+'/bddir.txt').read()
	temp = []
	gvar = {'using':{'dt': {'attrib': {'file': ['', ''], 'global': ['bool', 'True', {}], 'compile': ['bool', 'False', {}]}, 'code': "create var libdir array_item(dirsarray,'lib');create var packagedir array_item(dirsarray,'package');create var ld = B0;pyparse `var['pathdt'] = {'type':'bool','dt':Path('./.bdusingcompile/@{file}.cbd').is_file(),'headers':{}}`;if(pathdt){;create var dt = fread(`./.bdusingcompile/@{file}.cbd`);pyparse `var['dt']['type'] = 'binary'`;create var dt = dt.decode();};else{;if(exists usingpasswd){;create var passwd B1;};else{;create var passwd B0;};create class dt(static){;pyparse `try:\n\tif '''@{@fn}''' == '''@{file}''':\n\t\traise FileNotFoundError('')\n\telse:\n\t\topen('@{file}')\n\t\tparse(open('@{file}').read())\nexcept FileNotFoundError:\n\ttry:\n\t\topen('@{libdir}@{file}')\n\t\tvar['ld'] = {'type':'bool','dt':'True','headers':{}}\n\t\tparse(open('@{libdir}@{file}').read())\n\texcept FileNotFoundError:\n\t\ttry:\n\t\t\topen('@{packagedir}/@{file}/passwd.txt')\n\t\t\tif eval(var['passwd']['dt']):\n\t\t\t\tpasswd = base64.b64decode(open('@{packagedir}/@{file}/passwd.txt').read()).decode('utf-8')\n\t\t\t\tif var['usingpasswd']['dt'] == passwd:\n\t\t\t\t\tparse(open('@{packagedir}/@{file}/main.bd').read())\n\t\texcept:\n\t\t\tparse(open('@{packagedir}@{file}/main.bd').read())`;};};if(compile){;if(pathdt){;fwrite(`.bdusingcompile/@{file}.cbd`,tostring dt,'w');};else{;pyparse `os.mkdir('.bdusingcompile')`;fwrite(`.bdusingcompile/@{file}.cbd`,tostring dt,'w');};};if (ld){;foreach(n,f of dt){;pyparse\t`\nif 'req_pyparse' in var['dt']['dt'][var['n']['dt']]['dt']['head']:\n\tvar['dt']['dt'][var['n']['dt']]['dt']['head']['pyparse'] = 'true'\n`;};};if(global){;foreach(n,item of dt){;pyparse `gvar['@{n}'] = var['item']`;};};else{;return dt;}", 'head': {'global': '','pyparse':'true'}}, 'type': 'funct', 'headers': {}}, 'array_item': {'type': 'funct', 'dt': {'attrib': {'arr': ['', ''], 'cnt': ['', '']}, 'code': "\n\tcreate var data 'notdefined';\n\tpyparse `if var['cnt']['type'] == 'number':\n\tvar['cnt']['dt'] = int(var['cnt']['dt'])\nvar['data']['dt'] = var['arr']['dt'][var['cnt']['dt']]['dt']`;\n\treturn data\n", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '','pyparse':'true'}}}, 'eval': {'type': 'funct', 'dt': {'attrib': {'code': ['', '']}, 'code': "pyparse `parse('''@{code}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb','pyparse':'true'}}}, 'quit': {'type': 'funct', 'dt': {'attrib': {'status': ['number', 0.0]}, 'code': 'pyparse `quit(int(@{status}))`', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}, 'dirsarray': {'dt': {'bird': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/'}, 'lib': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/lib/'}, 'package': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/package/'}}, 'type': 'associative'}, 'fread': {'dt': {'attrib': {'fn': ['', '']}, 'code': 'pyparse `var[\'data\'] = {\'type\':\'string\',\'dt\':open("@{fn}").read()}`;return data', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'}, 'fwrite': {'dt': {'attrib': {'fn': ['', ''], 'txt': ['', ''], 'm': ['string', 'a']}, 'code': 'pyparse `d = open("""@{fn}""","""@{m}""")\nd.write("""@{txt}""")\nd.close()`;return true', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'}, 'fdelete': {'dt': {'attrib': {'fn': ['', '']}, 'code': "pyparse `import os\nos.remove('''@{fn}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'},'typeof':{'dt': {'attrib': {'item': ['', '']}, 'code': 'pyparse `var["data"] = {\'type\':\'string\',\'dt\':var[\'item\'][\'type\'],\'headers\':{}}`;return data', 'head': {'global': '', 'pyparse': 'true'}}, 'type': 'funct', 'headers': {}},'streval':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'string': ['', '']}, 'code': 'pyparse `tdt = typeify(""" @{string} """)\nvar[\'dt\'] = {"type":tdt[0],"dt":tdt[1],"headers":tdt[2]}`;return dt', 'head': {'pyparse': 'true'}}}}
	gvar['dirsarray'] = {'dt': {'bird': {'type': 'string', 'dt': bddir+'/'}, 'lib': {'type': 'string', 'dt': f'{bddir}/lib/'}, 'package': {'type': 'string', 'dt': f'{bddir}/package/'}}, 'type': 'associative','headers':{}}
	var = gvar
	classes = {}
	typedef = {}
	d = {'cnt':0,'ep':'','retd':'','break':False,'funct':False,'run':True,'els':False,'lastif':0,'interval':{},'class':'','atc':null,'ecnt':0,'atcd':'','atcdat':[],'lt':0,'errh':{},'clsd':{},'fn':'@main','tb':[],'pyparse':False,'version':'1.1.1','ctype':{'type':'null','dt':'null','headers':{}},'cfdat':0,'c':[],'gp':False}
def null(*args,**kwargs):
	pass
def error(n,t):
	try:
		parse(d['errh'][n])
	except:
		try:
			parse(d['errh']['Error'])
		except:
			print(f'{n} triggered at expression {str(d["cnt"]+1)}, file "{gvar["@fn"]["dt"]}", function "{d["fn"]}", command "{d["ep"]}": {t}\nTraceback:')
			if d['tb'] != []:
				for item in d['tb']:
					print('\t'+str(item))
			else:
				print('\t'+d['ep'])
			sys.exit(1)
def binary_encode(txt):
	import binascii
	global dta
	dta = bin(int(binascii.hexlify(txt.encode('utf-8', 'surrogatepass')), 16))[2:].zfill(8 * ((len(bin(int(binascii.hexlify(txt.encode('utf-8', 'surrogatepass')), 16))[2:]) + 7) // 8))
	dt = ' '.join([dta[i:i+8] for i in range(0, len(dta), 8)])
	del dta
	return dt
def typedat(dt):
	typ = dt[0]
	if typ == 'funct':
		dat = str(dt[1]).replace(';','\;')
		return {'code':{'type':'string','dt':dt[1]['code']},'allow':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'p': ['', '']}, 'code': "pyparse 'var['f'] = {'type':'"+dt[0]+"','dt':"+dat+",'headers':"+str(dt[2])+"}';if(p == 'pyparse'){;pyparse\t`if 'req_pyparse' in var['f']['dt']['head']:\n\tvar['f']['dt']['head']['pyparse'] = 'true'\n`;};return f", 'head': {'pyparse': 'true'}}}}
	elif typ == 'array':
		dat = dt[1].replace(";","\\;")
		return {'item':{'type': 'funct', 'dt': {'attrib': {'cnt': ['', '']}, 'code': f'create var arr {dat};create var data \'notdefined\';pyparse `if var[\'arr\'][\'type\'] == \'associative\' or var[\'arr\'][\'type\'] == \'array\':\n    if var[\'cnt\'][\'type\'] == \'number\':\n        var[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n    var[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']][\'dt\']\nelse:\n\tif var[\'cnt\'][\'type\'] == \'number\':\n\t\tvar[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n\tvar[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']]`;return data', 'head': {'pyparse': 'true'}}},'length':{'type':'number','dt':len(dt[1])-1}}
	elif typ == 'associative':
		tl = {'item':{'type': 'funct', 'dt': {'attrib': {'cnt': ['', ''],'arr':['associative',dt[1]]}, 'code': f'create var data \'notdefined\';pyparse `if var[\'arr\'][\'type\'] == \'associative\' or var[\'arr\'][\'type\'] == \'array\':\n    if var[\'cnt\'][\'type\'] == \'number\':\n        var[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n    var[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']][\'dt\']\nelse:\n\tif var[\'cnt\'][\'type\'] == \'number\':\n\t\tvar[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n\tvar[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']]`;return data', 'head': {'pyparse': 'true'}}}}
		for n,v in dt[1].items():
			tl[n] = v
		return tl
	else:
		tl = {'item':{'type': 'funct', 'dt': {'attrib': {'cnt': ['', '']}, 'code': f'create var arr "{dt[1]}";create var data \'notdefined\';pyparse `if var[\'arr\'][\'type\'] == \'associative\' or var[\'arr\'][\'type\'] == \'array\':\n    if var[\'cnt\'][\'type\'] == \'number\':\n        var[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n    var[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']][\'dt\']\nelse:\n\tif var[\'cnt\'][\'type\'] == \'number\':\n\t\tvar[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n\tvar[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']]`;return data', 'head': {'pyparse': 'true'}}},'length':{'type':'number','dt':len(dt[1])-1},'encode':{'type': 'funct', 'dt': {'attrib': {'encoding': ['', '']}, 'code': 'create var string "'+dt[1]+'";if (`"@{encoding}" == \'binary\'`){;pyparse `import binascii\nglobal dta\ndta = bin(int(binascii.hexlify(\'\'\'@{string}\'\'\'.encode(\'utf-8\', \'surrogatepass\')), 16))[2:].zfill(8 * ((len(bin(int(binascii.hexlify(\'\'\'@{string}\'\'\'.encode(\'utf-8\', \'surrogatepass\')), 16))[2:]) + 7) // 8))\ndt = \' \'.join([dta[i:i+8] for i in range(0, len(dta), 8)])\ndel dta\nvar[\'data\'] = {\'type\':\'binary\',\'dt\':dt}`;return data;}', 'head': {}}},'replace':{'type': 'funct', 'dt': {'attrib': {'old': ['', ''], 'new': ['', ''], 'cnt': ['string', '*']}, 'code': 'create var data "'+dt[1]+'";if (cnt == \'*\'){;pyparse `var[\'data\'][\'dt\'] = var[\'data\'][\'dt\'].replace(\'\'\'@{old}\'\'\',\'\'\'@{new}\'\'\')`;};else{;pyparse `var[\'data\'][\'dt\'] = var[\'data\'][\'dt\'].replace(\'\'\'@{old}\'\'\',\'\'\'@{new}\'\'\',int(@{cnt}))`;};return data', 'head': {'pyparse': 'true'}}},'group':{'type': 'funct', 'dt': {'attrib': {'data': ['', '']}, 'code': "create var o `"+dt[1]+"`;pyparse `var['dat'] = {'type':'string','dt':'''@{o}'''+'''@{data}'''}`;return dat", 'head': {'pyparse': 'true'}}}}
		if typ == 'binary':
			tl['decode'] = {'type': 'funct', 'dt': {'attrib': {'': ['', '']}, 'code': 'create var binary "'+dt[1]+'";pyparse `def text_to_bits(text, encoding=\'utf-8\', errors=\'surrogatepass\'):\n    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]\n    return bits.zfill(8 * ((len(bits) + 7) // 8))\ndef text_from_bits(bits, encoding=\'utf-8\', errors=\'surrogatepass\'):\n\timport binascii\n\ti = int(bits.replace(\' \',\'\'), 2)\n\thex_string = \'%x\' % i\n\tn = len(hex_string)\n\treturn binascii.unhexlify(hex_string.zfill(n + (n & 1))).decode(encoding, errors)\nvar[\'data\'] = {\'type\':\'string\',\'dt\':text_from_bits(\'@{binary}\')}`;return data', 'head': {'pyparse': 'true'}}}
		return tl
def clsrec(data,vd,appl):
	if len(data) == 1:
		return vd
	else:
		ndata = data
		data = str(data)
		ndata.pop(0)
		dat = clsrec(ndata,vd,appl[le(data)[0]])
		appl[le(data)[0]]['dt'][ndata[0]] = dat
		return appl
def mathify(code):
	dat = re.findall(r'[*/+\-%^]',code)
	for item in dat:
		if re.match(r'[ +\n\t]*\*[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) * float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
		elif re.match(r'[ +\n\t]*/[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) / float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
		elif re.match(r'[ +\n\t]*\+[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) + float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
		elif re.match(r'[ +\n\t]*\-[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) - float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
		elif re.match(r'[ +\n\t]*%[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) % float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
		elif re.match(r'[ +\n\t]*^[ +\n\t]*',item):
			data = code.split(item)
			code = code.replace(re.split(r'[*/+\-%^]',data[0])[0]+item+re.split(r'[*/+\-%^]',data[1])[0],str(float(typeify(re.split(r'[*/+\-%^]',data[0])[0])[1]) ** float(typeify(re.split(r'[*/+\-%^]',data[1])[0])[1])),1)
	return code
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
def re_to_list(dat):
	reml = []
	cnt = 0
	while True:
		try:
			reml.append(dat[cnt])
		except:
			break
		cnt += 1
	return reml
def log(data):
	opt = json.loads(open(f'{bddir}/pref/options.txt').read())
	if opt['logging']['log']:
		open(opt['logging']['logfile'],'a').write(data)
def typeify(txt,qt=False,err=True,ignore=False):
	txt = re.match(r'^[ +\n\t]*(.*)[ +\n\t]*$',txt,re.DOTALL)[1]
	h = {}
	if re.match(r'^[ +\n\t]*(.*)[ +\n\t]*===[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*===[ +\n\t]*',txt)
		if typeify(cv[0])[0] == typeify(cv[1])[0]:
			return ['bool',str(typeify(cv[0])[1] == typeify(cv[1])[1]),{}]
		else:
			return ['bool','False',{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*!==[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*!==[ +\n\t]*',txt)
		if typeify(cv[0])[0] == typeify(cv[1])[0]:
			return ['bool',str(typeify(cv[0])[1] != typeify(cv[1])[1]),{}]
		else:
			return ['bool','False',{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*>=[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*>=[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) >= str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*<=[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*<=[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) <= str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*>[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*>[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) > str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*<[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*<[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) < str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*==[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*==[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) == str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*(.*)[ +\n\t]*!=[ +\n\t]*(.*)[ +\n\t]*$',txt):
		cv = re.split(r'[ +\n\t]*!=[ +\n\t]*',txt)
		return ['bool',str(str(typeify(cv[0])[1]) != str(typeify(cv[1])[1])),{}]
	elif re.match(r'^[ +\n\t]*"(.*)"[ +\n\t]*(\:[ +\n\t]*[@]+){0,1}[ +\n\t]*$',txt,re.DOTALL):
		hd = re.match(r'^[ +\n\t]*"(.*)"[ +\n\t]*(\:[ +\n\t]*[@]+){0,1}[ +\n\t]*$',txt,re.DOTALL)
		txt = hd[1]
		hd = hd[2]
		if hd == None:
			h = []
		else:
			hd = re.sub(r'[ +\n\t]*\:[ +\n\t]*','',hd,1)
			h = []
			for char in hd:
				h.append(char)
		txt = re.sub(r'^[ +\n\t]*"','',txt,1)
		txt = re.sub(r'"[ +\n\t]*$','',txt,1)
		if not '@' in h:
			txt = bytes(txt, "utf-8").decode("unicode_escape")
		txt = txt.replace("'''",r"\'\'\'")
		ty = 'string'
		return [ty,txt,{}]
	elif re.match(r"^[ +\n\t]*'(.*)'[ +\n\t]*(\:[ +\n\t]*[@]+){0,1}[ +\n\t]*$",txt,re.DOTALL):
		hd = re.match(r"^[ +\n\t]*'(.*)'[ +\n\t]*(\:[ +\n\t]*[@]+){0,1}[ +\n\t]*$",txt,re.DOTALL)
		txt = hd[1]
		hd = hd[2]
		if hd == None:
			h = []
		else:
			hd = re.sub(r'[ +\n\t]*\:[ +\n\t]*','',hd,1)
			h = []
			for char in hd:
				h.append(char)
		ty = 'string'
		txt = re.sub(r"^[ +\n\t]*'",'',txt,1)
		txt = re.sub(r"'[ +\n\t]*$",'',txt,1)
		if not '@' in h:
			txt = bytes(txt, "utf-8").decode("unicode_escape")
		txt = txt.replace("'''",r"\'\'\'")
		return [ty,txt,{}]
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
					txt = txt.replace(f'@{{{dat[1]}}}',data)
				else:
					if dat[1] in var:
						if var[dat[1]]['type'] == 'funct':
							pass
						elif var[dat[1]]['type'] == 'class':
							txt = txt.replace(f'@{{{dat[1]}}}',str(var[dat[1]]['dt']['$value']['dt']))
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
		return [ty,txt,{}]
	elif re.match(r"^[ +\n\t]*[0-9.]+[ +\n\t]*$",txt):
		txt = float(txt)
		if str(txt).endswith('.0'):
			txt = int(txt)
		ty = 'number'
		return [ty,txt,{}]
	elif re.match(r'^[ \t\n]*$',txt):
		ty = 'null'
		txt = 'null'
		h = {}
		return [ty,txt,{}]
	elif re.match(r'^[ \t\n+]*null[ \t\n+]*$',txt,re.DOTALL):
		ty = 'null'
		txt = 'null'
		h = {}
		return [ty,txt,h]
	elif re.match(r'^[ \t\n+]*create[ \t\n+]+([a-zA-Z_]+[^@|\n\t (]*)[ \t\n+]*\((.*)\)',txt,re.DOTALL):
		dat = re.match(r'^[ \t\n+]*create[ \t\n+]+([a-zA-Z_]+[^@|\n\t (]*)[ \t\n+]*\((.*)\)',txt,re.DOTALL)
		n = dat[1]
		arg = dat[2]
		dt = var[n]
		gvar[n] = {'type':'class','dt':le(base64.b64decode(var[n]['dt']).decode('utf-8')),'headers':{}}
		var[n] = gvar[n]
		if 'this' in gvar:
			ot = gvar['this']
		else:
			ot = False
		gvar['this'] = var[n]
		parse(f'{n}.initiate({arg});')
		if ot:
			gvar['this'] = ot
		ty = 'class'
		txt = var[n]['dt']
		var[n] = dt
		gvar[n] = dt
	elif re.match(r'^[ \t\n]*([^\n\t ]+)\((.*)\)[ \t\n]*$',txt):
		oretd = d['retd']
		d['retd'] = ['null','null',{}]
		parse(txt)
		ret = d['retd']
		d['retd'] = oretd
		return ret
	elif re.match(r'[ +\t\n]*exists[ +\t\n]+(.*)[ +\t\n]*',txt):
		if typeify(re.match(r'[ +\t\n]*exists[ +\t\n]+(.*)[ +\t\n]*',txt)[1],err=False) == 'VE,UV':
			return ['bool','False',{}]
		else:
			return ['bool','True',{}]
	elif re.match(r'^[ +\t\n]*(\[.*\])[ +\t\n]*$',txt,re.DOTALL):
		it = str(le(re.match(r'^[ +\t\n]*(\[.*\])[ +\t\n]*$',txt,re.DOTALL)[1])[0])
		itd = ap(it.replace('[','',1)[::-1].replace(']','',1)[::-1])[::-1]+'['
		it = itd[::-1]+']'
		it = it.replace('\\c','\\comma')
		l = []
		for item in re.match(r'^[ +\t\n]*\[(.*)\][ +\t\n]*$',it,re.DOTALL)[1].split(','):
			item = item.replace('\\comma',',')
			l.append({'type':typeify(item)[0],'dt':typeify(item)[1]})
		txt = l
		ty = 'array'
		return [ty,txt,h]
	elif re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL):
		dt = re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL)
		dt = re.split(r'[ +\t\n]*[&+][ +\t\n]*',dt[1])
		l = {}
		for item in dt:
			dat = re.match('(.*)[:$](.*)',item,re.DOTALL)
			l[typeify(dat[1])[1]] = {'type':typeify(dat[2])[0],'dt':typeify(dat[2])[1]}
		txt = l
		ty = 'associative'
	elif re.match(r'^[ +\t\n]*{(.*)}[ +\t\n]*$',txt,re.DOTALL):
		dt = re.match(r'^[ +\t\n]*{(.*)}[ +\t\n]*$',txt,re.DOTALL)
		dat = dt[1].split(',')
		dt = re.split(r'[ +\t\n]*[,][ +\t\n]*',dt[1])
		l = {}
		for item in dt:
			dat = re.match('(.*)[:](.*)',item,re.DOTALL)
			l[typeify(dat[1])[1]] = {'type':typeify(dat[2])[0],'dt':typeify(dat[2])[1],'headers':typeify(dat[2])[2]}
		txt = l
		ty = 'associative'
		h = {}
		'''elif re.match(r'[ \t\n+]*funct[ \t\n+]*\((.*)\)\{(.*)\}[ +\t\n]*(\[.*\]){0,1}',txt,re.DOTALL):
		it = shfunct(re.match(r'[ \t\n+]*funct[ \t\n+]*\((.*)\)\{(.*)\}[ +\t\n]*(\[.*\]){0,1}',txt,re.DOTALL))
		txt = it['dt']
		ty = it['type']'''
		'''elif re.match(r'[ \t\n+]*tostring[ \t\n+]+(.*)[ \t\n+]*',txt,re.DOTALL):
		dt = re.match(r'[ \t\n+]*tostring[ \t\n+]+(.*)[ \t\n+]*',txt,re.DOTALL)
		dat = typeify(dt[1])
		if dat[0] == 'number':
			return ['string',str(dat[1])]
		elif dat[0] == 'class' or dat[0] == 'funct':
			return ['binary',binary_encode(str(dat[1])),{}]
		else:
			return ['string',str(dat[1]),{}]'''
	elif re.match(r'^[ \t\n+]*\\(.*)\\(.*)[ \t\n+]*$',txt,re.DOTALL):
			dt = re.match(r'^[ \t\n+]*\\(.*)\\(.*)[ \t\n+]*$',txt,re.DOTALL)
			dat = typeify(dt[2])
			typ = re.sub(r'[ \t\n+]*','',dt[1])
			if typ == 'string':
				if dat[0] == 'number':
					return ['string',str(dat[1]),{}]
				elif dat[0] == 'class' or dat[0] == 'funct':
					return ['binary',binary_encode(str(dat[1])),{}]
				else:
					return ['string',str(dat[1]),{}]
			elif typ == 'number':
				if dat[0] == 'string':
					ty = 'number'
					try:
						txt = float(dat[1])
						if str(txt).endswith('.0'):
							txt = int(txt)
					except:
						error('ConvertError','Cannot convert non-number to number.')
					h = dat[2]
			elif typ == 'array':
				if dat[0] == 'string':
					txt = []
					for char in dat[1]:
						txt.append({'type':'string','dt':char,'headers':{}})
					ty = 'array'
					h = {}
			else:
				error('ConvertError',f'Unknown Type: {typ}')
	elif re.match(r'^[ \t\n+]*(true|false|B1|B0)[ \t\n+]*$',txt):
		dt = re.match(r'[ \t\n+]*(true|false|B1|B0)[ \t\n+]*',txt)
		ty = 'bool'
		if dt[1] == 'true' or dt[1] == 'B1':
			txt = 'True'
		else:
			txt = 'False'
	elif re.match(r'^[ \t\n+]*(.+)([ +\n\t]*[*/\-+%^][ +\n\t]*(.+))+[ \t\n+]*$',txt,re.DOTALL):
		return typeify(str(mathify(txt)))
	else:
		for reg,fn in typedef.items():
			if(re.match('^'+reg+'$',txt,re.DOTALL)):
				dat = re.match('^'+reg+'$',txt,re.DOTALL)
				reml = []
				cnt = 0
				while True:
					try:
						reml.append(dat[cnt])
					except:
						break
					cnt += 1
				name = fn[1]
				fn = fn[0]
				d['ctype'] = {'dt':'null','headers':{}}
				v = {'txt':{'type':'string','dt':txt,'headers':{}}}
				cnt = 0
				for item in reml:
					v[f'@{str(cnt)}'] = {'type':'string','headers':{},'dt':item}
					cnt += 1
				cf(fn,v,{'pyparse':'true'})
				txt = d['ctype']['dt']
				h = d['ctype']['headers']
				if txt != 'null':
					ty = name
				else:
					ty = 'null'
				return [ty,txt,h]
		if '.' in txt:
			n = txt.split('.')
			dat = var
			cnt = 1
			for i in n:
				if cnt == len(n):
					ty = dat[i]['type']
					txt = dat[i]['dt']
				elif cnt == 1:
					dt = typeify(i)
					if dt[0] == 'class':
						dat = dt[1]
					else:
						dat = typedat(dt)
				else:
					if i in dat:
						if dat[i]['type'] == 'class':
							dat = dat[i]['dt']
				cnt += 1
		else:
			otxt = txt
			txt = re.sub(r'[ +\n\t]*','',txt)
			if txt in var.keys():
				ty = var[txt]['type']
				try:
					h = var[txt]['headers']
				except KeyError:
					var[txt]['headers'] = {'had_no_headers':True}
					h = {'had_no_headers':True}
				txt = var[txt]['dt']
			elif txt in gvar.keys():
				ty = gvar[txt]['type']
				try:
					h = gvar[txt]['head']
				except KeyError:
					gvar[txt]['headers'] = {'had_no_headers':True}
					h = {'had_no_headers':True}
				txt = gvar[txt]['dt']
			else:
				if err:
					#raise SyntaxError('')
					error('VarError',f'Unknown Var "{otxt}".')
				else:
					return 'VE,UV'
			if ty == 'reference':
				dt = typeify(txt)
				ty = dt[0]
				txt = dt[1]
				h = dt[2]
	return [ty,txt,h]
def cvar(regex):
	global var
	head = {}
	n = regex[3]
	'''if d['class'] != "":
		n = d['class']+n'''
	if regex[2]:
		for item in regex[3].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
			item = item.split('=')
			head[item[0]] = item[1]
	txt = regex[4]
	typ = typeify(txt)
	'''if 'debug_sethead' in head.keys():
		typ[2] = {'sethead':head['debug_sethead']}'''
	if re.match(r'^[ \t\n+]*&',n):
		typ[0] = 'reference'
		n = re.sub(r'^[ \t\n+]*&','',n,1)
		typ[1] = txt
	if d['class'] == '':
		if n.split('.')[0] == n:
			var[n] = {}
			var[n]['dt'] = typ[1]
			var[n]['type'] = typ[0]
			var[n]['headers'] = typ[2]
			if 'global' in head.keys():
				gvar[n] = {}
				gvar[n]['dt'] = typ[1]
				gvar[n]['type'] = typ[0]
				gvar[n]['headers'] = typ[2]
		else:
			var = clsrec(n.split('.'),{'type':typ[0],'dt':typ[1],'headers':typ[2]},var)
	else:
		'''for item in re.split(r'[ +\t\n]*.[ +\t\n]*'):
			var[item]['dt'] = '''
		n = d['class'] + n
		var = clsrec(n.split('.'),{'type':typ[0],'dt':typ[1],'headers':typ[2]},var)
def fatc(dt='',regex=[],tr=''): #Function ATC
	if dt != '':
		tr = re.match(r'[ +\t\n]*}[ +\t\n]*(\[.*\]){0,1}',tr)
		head = {}
		n = regex[1]
		if tr[1]:
			for item in tr[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
				item = item.split('=')
				head[item[0]] = item[1]
		if 'pyparse' in head:
			error('CreationError','Illegal header, pyparse.')
		if d['class'] == '':
			var[n]['dt'] = {'attrib':regex[2],'code':dt,'head':head}
			var[n]['headers']  = {}
			if 'global' in head.keys():
				gvar[n] = {'dt':{'attrib':regex[2],'code':dt,'head':head},'type':'funct','headers':{}}
		else:
			d['clsd'][d['class']][n] = {'type':'funct','dt':{'attrib':regex[2],'code':dt,'head':head},'headers':{}}
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
	var[n]['headers'] = {}
	args = {}
	re2 = ap(regex[2]).replace('\\c','\\comma')
	for item in re2.split(','):
		item = item.replace('\\comma',',')
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
	if d['pyparse'] or d['gp']:
		exec(typeify(regex[1],ignore=True)[1])
	else:
		error('PermissionError','Function does not have Pyparse Permissions.')
def cf(code,nvar,head,th={'type':'null','dt':'null','headers':{'null':'null'}}):
	global var
	dat = {}
	fn = ''
	dat['head'] = head
	dat['code'] = code
	nvar['this'] = th
	nvar['execution_data'] = {'type':'associative','dt':{},'headers':{}}
	odf = d['funct']
	ocnt = d['cnt']
	ofn = d['fn']
	d['tb'].append('Expression '+str(d['cnt'])+': '+d["ep"])
	d['fn'] = fn
	gvar['@cf']['dt'] = d['fn']
	d['cnt'] = 1
	d['funct'] = True
	ov = var
	var = nvar
	opyp = d['pyparse']
	if 'pyparse' in dat['head']:
		hp = dat['head']['pyparse']
		if dat['head']['pyparse'] == 'true':
			d['pyparse'] = True
		else:
			d['pyparse'] = False
	else:
		d['pyparse'] = False
		hp = 'false'
	parse(dat['code'])
	d['funct'] = odf
	d['cnt'] = ocnt
	del d['tb'][len(d['tb'])-1]
	d['fn'] = ofn
	gvar['@cf']['dt'] = d['fn']
	d['pyparse'] = opyp
	var = ov
	try:
		var[fn]['type'] = 'funct'
	except: 
		pass
	try:
		var[fn]['dt']['head']['pyparse'] = hp
	except:
		pass
def callfunct(regex):
	global var
	fn = regex[1]
	args = regex[2]
	if '.' in fn:
		txt = fn
		n = txt.split('.')
		dat = var
		th = {}
		cnt = 1
		lst = {}
		od = {}
		for i in n:
			if cnt == len(n):
				th = lst
				dat = dat[i]
			elif cnt == 1:
				try:
					lst = dat[i]
				except:
					pass
				dt = typeify(i)
				if dt[0] == 'class':
					dat = dt[1]
				else:
					dat = typedat(dt)
			else:
				try:
					lst = dat[i]
				except:
					pass
				if dat[i]['type'] == 'class':
					dat = dat[i]['dt']
			cnt += 1
	else:
		th = {'type':'null','dt':'null','headers':{'null':'null'}}
		try:
			dat = var[fn]
		except KeyError:
			error('VarError',f'Unknown var, "{fn}".')
	if not dat['type'] == 'funct':
		error('TypeError',f'Cannot call uncallable type: "{dat["type"]}".')
	for i,n in dat['dt'].items():
		dat[i] = n
	att = {}
	for i,n in dat['dt']['attrib'].items():
		att[i] = n
	cnt = 0
	nvar = gvar
	attl = []
	args = ap(args).replace('\\c','\\comma')
	for item in args.split(','):
		item = item.replace('\\comma',',')
		if item != '':
			item = typeify(item)
			attl.append(item)
	for i,n in att.items():
		try:
			attl[cnt]
		except IndexError:
			break
		nvar[i] = {'type':attl[cnt][0],'dt':attl[cnt][1],'headers':attl[cnt][2]}
		cnt += 1
	ncnt = 0
	for item,v in dat['attrib'].items():
		if ncnt >= cnt:
			if v != ['','']:
				nvar[item] = {'type':v[0],'dt':v[1],'headers':v[2]}
		ncnt += 1
	cf(dat['code'],nvar,dat['head'],th)
def cfaatc(codedat='',data=[],tr=''):
	global var
	regex = data[0]
	data = data[1]
	fn = regex[1]
	args = regex[2]
	if '.' in fn:
		txt = fn
		n = txt.split('.')
		dat = var
		th = {}
		cnt = 1
		lst = {}
		od = {}
		for i in n:
			if cnt == len(n):
				th = lst
				dat = dat[i]
			elif cnt == 1:
				lst = dat[i]
				dt = typeify(i)
				if dt[0] == 'class':
					dat = dt[1]
				else:
					dat = typedat(dt)
			else:
				lst = dat[i]
				if dat[i]['type'] == 'class':
					dat = dat[i]['dt']
			cnt += 1
	else:
		th = {'type':'null','dt':'null','headers':{'null':'null'}}
		try:
			dat = var[fn]
		except KeyError:
			error('VarError',f'Unknown var, "{fn}".')
	if not dat['type'] == 'funct':
		error('TypeError',f'Cannot call uncallable type: "{dat["type"]}".')
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
	attl.append(['funct',{'attrib': {'': ['', '']}, 'code': codedat,'head':{'cfa':True}},{}])
	for i,n in att.items():
		try:
			attl[cnt]
		except IndexError:
			break
		nvar[i] = {'type':attl[cnt][0],'dt':attl[cnt][1],'headers':attl[cnt][2]}
		cnt += 1
	ncnt = 0
	for item,v in dat['attrib'].items():
		if ncnt >= cnt:
			if v != ['','']:
				nvar[item] = {'type':v[0],'dt':v[1],'headers':v[2]}
		ncnt += 1
	cf(dat['code'],nvar,dat['head'],th)
def callfuncta(regex):
	d['ecnt'] = 1
	d['atcdat'] = [regex,[]]
	d['atc'] = cfaatc
def RETURN(regex):
	if d['funct']:
		d['retd'] = typeify(regex[1])
	else:
		error('ScopeError','Cannot use return outside of functions')
	return 'close'
def checkifs(cond):
	def test(d):
		'''if re.match(re.compile('^[ ]*[^\n=]+[ ]*==[ ]*[^\n=]+[ ]*$'),d):
			cv = re.split('[ ]*==[ ]*',d)
			return typeify(cv[0])[1] == typeify(cv[1])[1]
		elif re.match(r'^[ +\n\t]*(.+)[ +\n\t]*$',d):
			dt = re.match(r'^[ +\n\t]*(.+)[ +\n\t]*$',d)
			if eval(typeify(dt[1])[1]):
				return True
		elif d == "":
			return False
		else:
			raise SyntaxError(f'Invalid If-Statement, "{d}".')'''
		dt = typeify(d)
		if dt[0] == 'bool':
			return eval(str(dt[1]))
		else:
			if dt[1] != '':
				return True
			else:
				return False
	import re
	cond = re.split('[ ]*&&[ ]*',cond)
	for c in cond:
		if re.match(r'^[ \t\n+]*![ \t\n+]*',c):
			c = re.sub(r'^[ \t\n+]*![ \t\n+]*','',c)
			ret = False
			n = True
		else:
			ret = True
			n = False
		if len(re.split('[ ]*\|\|[ ]*',c)) != 1:
			t = False
			for cnd in re.split('[ ]*\|\|[ ]*',c):
				if test(cnd):
					t = True
					break
			if not t:
				return n
		else:
			if not test(c):
				return n
	return ret
def ifatc(dt='',data=[],tr=''):
	if dt != '':
		d['atcd'] = ''
		d['atc'] = null
		d['atcdat'] = []
		if checkifs(data[0]):
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
					var[dt[1]] = {'type':'number','dt':n,'headers':{}}
					parse(value)
			elif v[0] == 'array':
				for i in v[1]:
					var[dt[1]] = i
					parse(value)
			else:
				for i in v[1]:
					var[dt[1]] = {'type':'string','dt':i,'headers':{}}
					parse(value)
		else:
			v = typeify(dt[3])
			if v[0] == 'associative':
				for i in v[1].keys():
					var[dt[1]] = {'type':'string','dt':i,'headers':{}}
					parse(value)
			elif v[0] == 'class':
				data = re.split(r'[ +\n\t]*,[ +\n\t]*',dt[1])
				for i,n in v[1].items():
					var[data[0]] = {'type':'string','dt':i,'headers':{}}
					var[data[1]] = n
					parse(value)
	else:
		return 'a'
def foreach(regex):
	dt = re.match(r'([a-zA-Z_]+[^|.\n\t ]*)[ +\n\t]+(in|of)[ +\n\t]+(.*)',regex[1])
	d['ecnt'] = 1
	d['atcdat'] = dt
	d['atc'] = featc
def whatc(value='',regex=[],tr=''):
	while checkifs(regex[1]):
		parse(value)
def whileloop(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = whatc
def whenatc(value='',regex=[],tr=''):
	#l = ['',regex[1],value,head]
	l = ['',regex[1],value]
	def when_wrapper(reg):
		if checkifs(reg[1]):
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
	for item in re2.split(','):
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
		head = {}
		if tr[1]:
			for item in tr[1].replace('[','',1)[::-1].replace(']','',1)[::-1].split('&'):
				item = item.split('=')
				head[item[0]] = item[1]
		typ = data[2]
		if typ == 'instance':
			var[data[1]] = {'type':'class','dt':{},'headers':{}}
		else:
			var[data[1]] = {'type':'class','dt':{},'headers':{}}
		ocls = d['class']
		d['class'] = data[1]+'.'
		d['clsd'][d['class']] = {}
		parse(code)
		if typ == 'static':
			var[data[1]]['dt'] = d['clsd'][d['class']]
		else:
			var[data[1]]['dt'] = base64.b64encode(str.encode(str(d['clsd'][d['class']])))
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
def allow(regex):
	p = regex[2]
	n = regex[1]
	nd = var[n]
	if p == 'pyparse':
		if 'req_pyparse' in nd['dt']['head']:
			var[n]['dt']['head']['pyparse'] = 'true'
def deny(regex):
	p = regex[2]
	n = regex[1]
	nd = var[n]
	if p == 'pyparse':
		if 'req_pyparse' in nd['dt']['head']:
			if 'pyparse' in nd['dt']['head']:
				del var[n]['dt']['head']['pyparse']
def rsc(regex):
	n = regex[1]
	nd = var[n]
	nd['dt'] = nd['dt'].replace(';','\;')
def ctatc(dt='',regex=[],tr=''):
	typedef[typeify(regex[2])[1]] = [dt,regex[1]]
def ctype(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = ctatc
def ccatc(dt='',regex=[],tr=''):
	cl[typeify(regex[2])[1]] = [dt,regex[1]]
def ccmd(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = ccatc
cl = {r'[ +\t\n]*(create[ +\t\n]+|)var(\[.*\]){0,1}[ +\t\n]*([a-zA-Z_&]+[^@|\n\t ]*)[ +\t\n]*[=]{0,1}[ +\t\n]*(.*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)[ +\t\n]*':[pyparse,'Pyparse'],r'[ +\t\n]*([^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*':[callfunct,'Call Function'],r'[ +\t\n]*return[ +\t\n]*([^\n]*)':[RETURN,'Return'],r'[ +\t\n]*(if|else[ +]if)[ +\t\n]*\((.*)\)[ +\t\n]*\{':[ifstate,'If Statement'],r'[ +\t\n]*else[ +\t\n]*\{':[els,'Else'],r'[ +\t\n]*foreach[ +\t\n]*\((.*)\)[ +\t\n]*\{':[foreach,'Foreach Loop'],r'[ +\t\n]*while[ +\t\n]*\((.*)\)[ +\t\n]*\{':[whileloop,'While Loop'],r'[ +\t\n]*when[ +\t\n]*\((.*)\)[ +\t\n]*\{':[when,'When Loop'],r"^[ +\t\n]*$":[null,'WhiteSpace'],r"[ +\t\n]*create[ +\t\n]+class[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\([ +\t\n]*(instance|static)[ +\t\n]*\)[ +\t\n]*\{":[cla,'Class'],r'[ +\t\n]*create ErrorHandler[ +\t\n]*\((.*)\)[ +\t\n]*\{':[errh,"Create Error Handler"],r'[ +\t\n]*global[ +\t\n]*(.*)[ +\t\n]*':[globalize,'Global'],r'[ +\t\n]*([^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[callfuncta,'Call Function With Attach'],r'[ +\t\n]*allow[ +\t\n]+([^ ]+)[ +\t\n]*:[ +\t\n]*([^ ]+)[ +\t\n]*':[allow,'Allow'],r'[ +\t\n]*deny[ +\t\n]+([^ ]+)[ +\t\n]*:[ +\t\n]*([^ ]+)[ +\t\n]*':[deny,'Deny'],r'[ +\t\n]*rsc[ +\t\n]+([^\n \t]+)[ +\t\n]*':[rsc,'Replace Semicolon'],r'[ +\n\t]*create[ +\n\t]+type[ +\n\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[ctype,'Custom Type Creator'],r'[ +\n\t]*create[ +\n\t]+command[ +\n\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[ccmd,'Custom Command Creator']}
ccl = {}
for item,dt in cl.items():
	ccl[dt[1]] = dt[0]
def parse(code):
	code = code.replace('\\;','\\semi')
	code = re.sub(r'\/\/[^/]*\/\/','',code,re.DOTALL)
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
							log(funct[1]+'\n')
							if d['fn'] == '@main':
								clvd = [funct[1]]
								clvd.append(re_to_list(re.match('^'+reg+'$',line,re.DOTALL)))
								d['c'].append(clvd)
							if type(funct[0]) == str:
								txt = line
								fn = funct
								dat = re.match('^'+reg+'$',txt,re.DOTALL)
								reml = []
								cnt = 0
								while True:
									try:
										reml.append(dat[cnt])
									except:
										break
									cnt += 1
								name = fn[1]
								fn = fn[0]
								v = {'txt':{'type':'string','dt':txt,'headers':{}}}
								cnt = 0
								for item in reml:
									v[f'@{str(cnt)}'] = {'type':'string','headers':{},'dt':item}
									cnt += 1
								ocfd = d['cfdat']
								d['cfdat'] = 0
								cf(fn,v,{'pyparse':'true'})
								dat = d['cfdat']
								d['cfdat'] = ocfd
								if dat == 1:
									return 'end'
								fnd = True
								break
							else:
								dat = funct[0](re.match('^'+reg+'$',line,re.DOTALL))
								if dat == 'close':
									return 'end'
								fnd = True
								break
					if not fnd:
						error('SyntaxError',f'No Such Command, {line}.')
					if not d['funct']:
						for item in temp:
							del var[item]
				d['cnt'] += 1
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
def uncompile(cc):
	cc = le(str(cc))
	
def console():
	code = ''
	ll = ''
	while True:
		try:
			ic = input('>>> ')
			if ic == 'rewrite_lastline':
				code = code[::-1].replace(ll[::-1],'',1)[::-1]
			elif ic == 'ccrll':
				code = code[::-1].replace(ll[::-1],'',1)[::-1]
			elif ic == 'ccexit':
				print('')
				return code
			else:
				if not re.match(r';[ +\t\n]*$',ic):
					ic += ';'
				ll = ic
				code += ic
		except KeyboardInterrupt:
			print('')
			return code
def ic(asu=True):
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', type=str, nargs='?')
	parser.add_argument('-a', action='store_true')
	parser.add_argument('--autoexec', action='store_true')
	parser.add_argument('-c', action='store_true')
	parser.add_argument('-pp', action='store_true')
	parser.add_argument('-p', action='store_true')
	parser.add_argument('--pyparse', action='store_true')
	parser.add_argument('--globalpyparse', action='store_true')
	parser.add_argument('--bddir', type=str)
	args = parser.parse_args()
	if asu:
		if args.bddir:
			su(args.bddir)
		else:
			su()
	if args.p or args.pyparse:
		d['pyparse'] = True
	if args.pp or args.globalpyparse:
		d['gp'] = True
	if not args.a and not args.autoexec:
		gvar['@fn'] = {'type':'string','dt':bddir+'/pref/autoexec.bd','headers':{}}
		gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
		gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
		gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
		gvar['@license'] = {'type':'string','dt':open(bddir+'/LICENSE').read(),'headers':{}}
		with open(bddir+'/pref/autoexec.bd') as data:
			parse(data.read())
	if not args.c:
		if args.filename:
			fn = args.filename
			d['cnt'] = 0
			gvar['@fn'] = {'type':'string','dt':Path(fn).absolute(),'headers':{}}
			parse(open(fn).read())
		else:
			d['cnt'] = 0
			print(f'Bird Programming Language {d["version"]}\nCopyright (C) 2021\nType \'writeout(@license)\' to see license.')
			gvar['@fn'] = {'type':'string','dt':'<input>','headers':{}}
			parse(console())
	else:
		fn = args.filename
		d['cnt'] = 0
		gvar['@fn'] = {'type':'string','dt':Path(fn).absolute(),'headers':{}}
		uncompile(open(fn).read())
def replit(asu=True):
	if asu:
		su()
	print(f'Bird Programming Language {d["version"]}\nCopyright (C) 2021')
	fn = input('Filename: ')
	gvar['@fn'] = {'type':'string','dt':Path(fn).absolute(),'headers':{}}
	gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
	gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
	gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
	gvar['@license'] = {'type':'string','dt':open(bddir+'/LICENSE').read(),'headers':{}}
	with open(bddir+'/pref/autoexec.bd') as data:
		parse(data.read())
	d['cnt'] = 0
	chdir('tests/')
	parse(open(fn).read())