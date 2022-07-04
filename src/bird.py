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
import json
def ap(text,cchar=','):
	latc = [False]
	atct = []
	txt = []
	for item in text:
		txt.append(item)
	text = ''
	cnt = 0
	lc = {'(':')','[':']','"':'"',"'":"'",'`':'`'}
	for char in txt:
		if latc[0]:
			if lc[atct[0]] == char:
				del latc[0]
			if char == cchar:
				text += '\\c'
			else:
				text += char
		else:
			if char in lc.keys():
				latc.insert(0,True)
				atct.insert(0,char)
			text += char
		cnt += 1
	return text
def su(home=str(Path.home())):
	global bddir
	global temp
	global gvar
	global opt
	global var
	global d
	global typedef
	global opt
	global sgv
	bddir = open(home+'/bddir.txt').read()
	temp = []
	gvar = {'using':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'file': ['', ''], 'global': ['bool', 'True', {}], 'compile': ['bool', 'False', {}]}, 'code': 'CNCHEADER6 file;CNCHEADER6 global;CNCHEADER6 compile;CNC6', 'head': {}}}, 'array_item': {'type': 'funct', 'headers': {}, 'dt': {'attrib': {'arr': ['', ''], 'cnt': ['', '']}, 'code': 'var data = null;CNC15;return data', 'head': {'gvar': 'true'}}}, 'eval': {'type': 'funct', 'headers': {}, 'dt': {'attrib': {'code': ['', '']}, 'code': 'CNCHEADER16 code;CNC16', 'head': {}}}, 'quit': {'type': 'funct', 'headers': {}, 'dt': {'attrib': {'code': ['number', 0, {}]}, 'code': 'CNCHEADER17 code;CNC17', 'head': {}}}, 'fread':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'filename': ['', '']}, 'code': 'CNCHEADER18 filename;CNC18;return data', 'head': {}}}, 'fwrite': {'type': 'funct', 'headers': {}, 'dt': {'attrib': {'fn': ['', ''], 'txt': ['', ''], 'overwite': ['bool', 'False', {}]}, 'code': 'CNCHEADER19 fn;CNCHEADER19 txt;CNCHEADER19 overwite;CNC19;return true', 'head': {}}}, 'fdelete': {'type': 'funct', 'headers': {}, 'dt': {'attrib': {'name': ['', '']}, 'code': 'CNCHEADER20 name;CNC20;return name', 'head': {}}},'typeof':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'item': ['', '']}, 'code': 'CNC21;return typ', 'head': {}}},'streval':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'txt': ['', '']}, 'code': 'CNCHEADER22 txt;CNC22;return dt', 'head': {}}},"concat":{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'v1': ['', ''], 'v2': ['', '']}, 'code': 'CNCHEADER27 v1;CNCHEADER27 v2;CNC27;return dat', 'head': {'gvar': 'true'}}}}
	gvar['dirsarray'] = {'dt': {'bird': {'type': 'string', 'dt': bddir+'/'}, 'lib': {'type': 'string', 'dt': f'{bddir}/lib/'}, 'package': {'type': 'string', 'dt': f'{bddir}/package/'}}, 'type': 'associative','headers':{},'getpermissions':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'fn': ['', '']}, 'code': 'CNCHEADER23 fn;CNC23;return dat', 'head': {'gvar': 'true'}}}}
	sgv = gvar
	var = gvar
	typedef = {}
	d = {'cnt':0,'ep':'','retd':'','break':False,'funct':False,'run':True,'els':False,'lastif':0,'interval':{},'class':'','atc':null,'ecnt':0,'atcd':'','atcdat':[],'lt':0,'errh':{},'clsd':{},'fn':'@main','tb':[],'pyparse':False,'version':'1.2.1 Pre Release','ctype':{'type':'null','dt':'null','headers':{}},'cfdat':0,'c':[],'gp':False,'bddir':bddir,'lcd':False,'swd':'','sw':False,'sdef':False,'cncheaders':{},'ignorewarnings':False,"extraargs":[]}
	opt = json.loads(open(f'{bddir}/pref/options.txt').read())
def null(*args,**kwargs):
	pass
def error(n,t,warning=False):
	ex = True
	if warning:
		if d['ignorewarnings']:
			return True
		else:
			if not opt['warning']['exit']:
				ex = False
	try:
		parse(d['errh'][n])
	except:
		try:
			parse(d['errh']['Error'])
		except:
			tx = ''
			tx += f'{n} triggered at expression {str(d["cnt"]+1)}, file "{gvar["@fn"]["dt"]}", function "{d["fn"]}", command "{d["ep"]}": {t}\nTraceback:'+'\n'
			if d['tb'] != []:
				for item in d['tb']:
					tx += '\t'+str(item) + '\n'
			else:
				tx += '\t'+d['ep'] + '\n'
			p = True
			if warning:
				if opt['warning']['log']:
					if opt['warning']['tologfile']:
						log(tx)
					else:
						open(opt['warning']['logfile'],'a').write(tx)
				if not opt['warning']['toconsole']:
					p = False
			if p:
				print(tx)
			if ex:
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
		return {'code':{'type':'string','dt':dt[1]['code']}}
	elif typ == 'array':
		dat = str(dt[1]).replace(";","\\;")
		return {'item':{'type': 'funct', 'dt': {'attrib': {'cnt': ['', '']}, 'code': f'pyparse `var["arr"] = {{"type":"array","dt":{dat},"headers":{{}}}}`;create var data \'notdefined\';pyparse `if var[\'arr\'][\'type\'] == \'associative\' or var[\'arr\'][\'type\'] == \'array\':\n    if var[\'cnt\'][\'type\'] == \'number\':\n        var[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n    var[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']][\'dt\']\nelse:\n\tif var[\'cnt\'][\'type\'] == \'number\':\n\t\tvar[\'cnt\'][\'dt\'] = int(var[\'cnt\'][\'dt\'])\n\tvar[\'data\'][\'dt\'] = var[\'arr\'][\'dt\'][var[\'cnt\'][\'dt\']]`;return data', 'head': {'pyparse': 'true'}}},'length':{'type':'number','dt':len(dt[1])-1}}
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
		h = {'null':'ws'}
		return [ty,txt,{}]
	elif re.match(r'^[ \t\n+]*null[ \t\n+]*$',txt,re.DOTALL):
		ty = 'null'
		txt = 'null'
		h = {'null':'null'}
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
		#it = str(le(re.match(r'^[ +\t\n]*(\[.*\])[ +\t\n]*$',txt,re.DOTALL)[1])[0])
		it = txt
		itd = ap(it.replace('[','',1)[::-1].replace(']','',1)[::-1])[::-1]
		it = itd[::-1]
		it = it.replace('\\c','\\comma')
		l = []
		for item in re.split('[ +\t\n]*,[ +\t\n]*',it):
			item = item.replace('\\comma',',')
			t = typeify(item)
			l.append({'type':t[0],'dt':t[1],'headers':t[2]})
		if l == [{'type': 'null', 'dt': 'null', 'headers': {}}]:
			l = []
		txt = l
		ty = 'array'
		return [ty,txt,h]
	elif re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL):
		dt = re.match(r'^[ +\t\n]*aa[ +\t\n]+(.*)[ +\t\n]*$',txt,re.DOTALL)
		dt = re.split(r'[ +\t\n]*[&+][ +\t\n]*',dt[1])
		l = {}
		for item in dt:
			dat = re.match('(.*)[:$](.*)',item,re.DOTALL)
			l[typeify(dat[1])[1]] = {'type':typeify(dat[2])[0],'dt':typeify(dat[2])[1],'headers':{}}
		txt = l
		ty = 'associative'
		h = {}
	elif re.match(r'^[ +\t\n]*{(.*)}[ +\t\n]*$',txt,re.DOTALL):
		dt = re.match(r'^[ +\t\n]*{(.*)}[ +\t\n]*$',txt,re.DOTALL)
		dat = ap(dt[1]).replace('\\c','\\comma').split(',')
		dt = re.split(r'[ +\t\n]*[,][ +\t\n]*',ap(dt[1]).replace('\\c','\\comma'))
		l = {}
		if dt != [""]:
			for item in dt:
				dat = re.match('(.*)[:](.*)',item,re.DOTALL)
				l[typeify(dat[1].replace('\\comma',','))[1]] = {'type':typeify(dat[2].replace('\\comma',','))[0],'dt':typeify(dat[2].replace('\\comma',','))[1],'headers':typeify(dat[2].replace('\\comma',','))[2]}
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
					error('ConvertError',f'Cannot convert {dat[0]} to {typ}.')
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
				else:
					error('ConvertError',f'Cannot convert {dat[0]} to {typ}.')
			elif typ == 'array':
				if dat[0] == 'string':
					txt = []
					for char in dat[1]:
						txt.append({'type':'string','dt':char,'headers':{}})
					ty = 'array'
					h = {}
				else:
					error('ConvertError',f'Cannot convert {dat[0]} to {typ}.')
			elif typ == 'storage':
				return ['binary',binary_encode(str(dat[1])),{}]
			else:
				error('ConvertError',f'Unknown Type: {typ}')
	elif re.match(r'^[ \t\n+]*(true|false|B1|B0|True|False)[ \t\n+]*$',txt):
		dt = re.match(r'[ \t\n+]*(true|false|B1|B0|True|False)[ \t\n+]*',txt)
		ty = 'bool'
		if dt[1].lower() == 'true' or dt[1] == 'B1':
			txt = 'True'
		else:
			txt = 'False'
	elif re.match(r'^[ \t\n+]*(.+)([ +\n\t]*[*/\-+%^][ +\n\t]*.+)+[ \t\n+]*$',txt,re.DOTALL):
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
		elif 'gvar' in head:
			error('CreationError','Illegal header, gvar.')
		head['gvar'] = 'true'
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
	error('DepricationWarning','As of Version 1.2.0, Pyparse is now depricated.',True)
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
	try:
		dat['head']['stararg']
		star = True
	except:
		star = False
	sal = {'type':'array','dt':[],'headers':{'stararg':'true'}}
	att = {}
	for i,n in dat['dt']['attrib'].items():
		att[i] = n
	cnt = 0
	if 'gvar' in dat['head']:
		if dat['head']['gvar'] == 'false':
			nvar = sgv
		else:
			nvar = gvar
	else:
		nvar = gvar
	attl = []
	args = ap(args).replace('\\c','\\comma')
	for item in args.split(','):
		item = item.replace('\\comma',',')
		if item != '':
			item = typeify(item)
			attl.append(item)
	if star:
		sal['st'] = attl
		nvar[dat['head']['stararg']] = sal
	else:
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
	if 'gvar' in dat['head']:
		if dat['head']['gvar'] == 'false':
			nvar = sgv
		else:
			nvar = gvar
	else:
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
	elif p == 'gvar':
		var[n]['dt']['head']['gvar'] = 'true'
def deny(regex):
	p = regex[2]
	n = regex[1]
	nd = var[n]
	if p == 'pyparse':
		if 'req_pyparse' in nd['dt']['head']:
			if 'pyparse' in nd['dt']['head']:
				del var[n]['dt']['head']['pyparse']
	elif p == 'gvar':
		var[n]['dt']['head']['gvar'] = 'false'
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
def swatc(dt='',data=[],tr=''):
	oswd = d['swd']
	osw = d['sw']
	d['swd'] = data[1]
	d['sw'] = True
	parse(dt)
	d['swd'] = oswd
	d['sw'] = osw
def switch(regex):
	d['ecnt'] = 1
	d['atcdat'] = regex
	d['atc'] = swatc
def caseatc(dt='',dat=[],tr=''):
	data = dat[0]
	if dat[1]:
		if d['sdef']:
			parse(dt)
	else:
		if data:
			parse(dt)
		else:
			d['sdef'] = True
def case(regex):
	if not d['sw']:
		error('SwitchError','Case called while not inside Switch block.')
	defa = False
	if re.match('^[ +\t\n]*$',regex[3]):
		defa = True
	hl = []
	if regex[1]:
		for char in regex[2]:
			hl.append(char)
	if '!' in hl:
		dat = checkifs(f'{d["swd"]} != {regex[3]}')
	elif '=' in hl:
		dat = checkifs(f'{d["swd"]} === {regex[3]}')
	else:
		dat = checkifs(f'{d["swd"]} == {regex[3]}')
	d['ecnt'] = 1
	d['atcdat'] = [dat,defa]
	d['atc'] = caseatc
def binary_decode(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
def cnc(regex):
	number = int(regex[1])
	try:
		data = d['cncheaders'][number]
	except KeyError:
		pass
	if number == 1:
		print('CNC Help.')
		print('CNC (Call Number Call) is for running python commands without using the insecure pyparse.')
		print('You enter a call number and the command associated with that call number is called.')
		print('Call numbers are always Intagers.')
		print('To add a Call Number, make an issue at the mathstar13/bird github.')
	elif number == 3:
		print(data[0],end=data[1],flush=eval(data[2]))
	elif number == 4:
		dat = input(data[0])
		var['data'] = {'type':'string','dt':dat,'headers':{}}
	elif number == 5:
		var['dt'] = {'type':'bool','dt':str(Path(data[0]).is_dir()),'headers':{}}
	elif number == 6:
		libdir = f'{bddir}/lib/'
		packagedir = f'{bddir}/package/'
		file = data[0]
		glo = data[1]
		comp = data[2]
		ld = False
		#parse('create class dat(static){')
		if(Path(f'./.bdusingcompile/{file}.cbd').is_file()):
			parse(binary_decode(open('/.bdusingcompile/{file}.cbd').read()))
		else:
			try:
				if file == d['filename']:
					raise FileNotFoundError('')
				else:
					open(file)
					parse(open(file).read())
			except FileNotFoundError:
				try:
					open(f'{libdir}{file}')
					ld = True
					parse(open(f'{libdir}{file}').read())
				except FileNotFoundError:
					try:
						open(f'{packagedir}{file}/main.bd')
						parse(open(f'{packagedir}{file}/main.bd').read())
					except FileNotFoundError:
						error('UsingError',f'Cannot use file "{file}".')
		"""if ld:
			parse('''foreach(n,f of dat){\npyparse `\nif 'req_pyparse' in var['dat']['dt'][var['n']['dt']]['dt']['head']:\n\tvar['dat']['dt'][var['n']['dt']]['dt']['head']['pyparse'] = 'true'`;};''')"""
		#if glo:
		#	#parse('''foreach(n,item of dat){pyparse `gvar['@{n}'] = var['item']`;};''')
		#	parse('''foreach(n,item of dat){writeout(n);}''')
		#	var['ret'] = {'type':'bool','dt':'False','headers':{}}
		#else:
		#	var['ret'] = {'type':'bool','dt':'True','headers':{}}
		#parse('};')
	elif number == 7:
		if os.name == 'nt':
			os.system(f'explorer {data[0]}')
		else:
			os.system(f'open {data[0]}')
	elif number == 8:
		import time
		time.sleep(int(data[0]))
	elif number == 9:
		var['dat'] = {'type':'string','dt':os.name,'headers':{}}
	elif number == 10:
		os.system(data[0])
	elif number == 11:
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	elif number == 12:
		import math
		var['data'] = {'type':'number','dt':math.sqrt(int(data[0])),'headers':{}}
	elif number == 13:
		da = str.encode(data[0])
		var["data"] = {"type":'string','dt':base64.b64encode(da).decode('utf-8'),'headers':{}}
	elif number == 14:
		var["data"] = {"type":'string','dt':base64.b64decode(str.encode(data[0])).decode('utf-8'),'headers':{}}
	elif number == 15:
		if var['cnt']['type'] == 'number':
			var['cnt']['dt'] = int(var['cnt']['dt'])
		var['data']['dt'] = var['arr']['dt'][var['cnt']['dt']]['dt']
	elif number == 16:
		parse(data[0])
	elif number == 17:
		sys.exit(data[0])
	elif number == 18:
		var['data'] = {'type':'string','dt':open(data[0]).read(),'headers':{}}
	elif number == 19:
		if eval(data[2]):
			dat = open(data[0],'w')
			dat.write(data[1])
			dat.close()
		else:
			dat = open(data[0],'a')
			dat.write(data[1])
			dat.close()
	elif number == 20:
		os.remove(data[0])
	elif number == 21:
		var["typ"] = {'type':'string','dt':var['item']['type'],'headers':{}}
	elif number == 22:
		tdt = typeify(data[0])
		var['dt'] = {"type":tdt[0],"dt":tdt[1],"headers":tdt[2]}
	elif number == 23:
		data = data[0]['head']
		dat = {}
		if 'pyparse' in data:
			dat['pyparse'] = data['pyparse']
		if 'gvar' in data:
			dat['gvar'] = data['gvar']
		parse(f'var dat = {str(dat)}')
	elif number == 24:
		print(var)
	elif number == 25:
		var['dt'] = {'type':'bool','dt':str(Path(data[0]).is_file()),'headers':{}}
	elif number == 26:
		par = data[0]
		pars = argparse.ArgumentParser()
		for item,v in par.items():
			i = {}
			if "nargs" in v['dt'].keys():
				i["nargs"] = v["dt"]["nargs"]["dt"]
			else:
				i["nargs"] = 1
			pars.add_argument(item,nargs=i["nargs"])
		vd = vars(pars.parse_args(d["extraargs"]))
		var["dat"] = {}
		dta = typeify(str(vd))
		var["dat"]["type"] = dta[0]
		var["dat"]["dt"] = dta[1]
		var["dat"]["headers"] = dta[2]
	elif number == 27:
		var['dat'] = {"type":"string","dt":data[0]+data[1],"headers":{}}
	d['cncheaders'][number] = []
def cnch(regex):
	n = int(regex[1])
	try:
		d['cncheaders'][n]
	except:
		d['cncheaders'][n] = []
	d['cncheaders'][n].append(typeify(regex[2])[1])
cl = {r'[ +\t\n]*(create[ +\t\n]+|)var(\[.*\]){0,1}[ +\t\n]*([a-zA-Z_&]+[^@|\n\t ]*)[ +\t\n]*[=]{0,1}[ +\t\n]*(.*)''':[cvar,'Create Var'],r'[ +\t\n]*create[ +\t\n]+funct[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[cfunct,'Create Function'],r'//.*//':[null,'Comment'],r'[ +\t\n]*pyparse[ +\t]+(.*)[ +\t\n]*':[pyparse,'Pyparse'],r'[ +\t\n]*([^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*':[callfunct,'Call Function'],r'[ +\t\n]*return[ +\t\n]*([^\n]*)':[RETURN,'Return'],r'[ +\t\n]*(if|else[ +]if)[ +\t\n]*\((.*)\)[ +\t\n]*\{':[ifstate,'If Statement'],r'[ +\t\n]*else[ +\t\n]*\{':[els,'Else'],r'[ +\t\n]*foreach[ +\t\n]*\((.*)\)[ +\t\n]*\{':[foreach,'Foreach Loop'],r'[ +\t\n]*while[ +\t\n]*\((.*)\)[ +\t\n]*\{':[whileloop,'While Loop'],r'[ +\t\n]*when[ +\t\n]*\((.*)\)[ +\t\n]*\{':[when,'When Loop'],r"^[ +\t\n]*$":[null,'WhiteSpace'],r"[ +\t\n]*create[ +\t\n]+class[ +\t\n]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\t\n]*\([ +\t\n]*(instance|static)[ +\t\n]*\)[ +\t\n]*\{":[cla,'Class'],r'[ +\t\n]*create ErrorHandler[ +\t\n]*\((.*)\)[ +\t\n]*\{':[errh,"Create Error Handler"],r'[ +\t\n]*global[ +\t\n]*(.*)[ +\t\n]*':[globalize,'Global'],r'[ +\n\t]*switch[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[switch,'Switch'],r'[ +\n\t]*case[ +\n\t]*(:([^(])){0,1}[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[case,'Case'],r'[ +\t\n]*([^@|\n\t (]*)[ +\t\n]*\((.*)\)[ +\t\n]*\{[ +\t\n]*':[callfuncta,'Call Function With Attach'],r'[ +\t\n]*allow[ +\t\n]+([^ ]+)[ +\t\n]*:[ +\t\n]*([^ ]+)[ +\t\n]*':[allow,'Allow'],r'[ +\t\n]*deny[ +\t\n]+([^ ]+)[ +\t\n]*:[ +\t\n]*([^ ]+)[ +\t\n]*':[deny,'Deny'],r'[ +\t\n]*rsc[ +\t\n]+([^\n \t]+)[ +\t\n]*':[rsc,'Replace Semicolon'],r'[ +\n\t]*create[ +\n\t]+type[ +\n\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[ctype,'Custom Type Creator'],r'[ +\n\t]*create[ +\n\t]+command[ +\n\t]+([a-zA-Z_]+[^@|.\n\t ]*)[ +\n\t]*\((.*)\)[ +\n\t]*\{[ +\n\t]*':[ccmd,'Custom Command Creator'],r'[ +\n\t]*CNC[ +\n\t]*([0-9]+)[ +\n\t]*':[cnc,'Call Number Call'],r'[ +\n\t]*CNCHEADER[ +\n\t]*([0-9]+)[ +\n\t]*(.*)[ +\n\t]*':[cnch,'Call Number Call Header']}
ccl = {}
for item,dt in cl.items():
	ccl[dt[1]] = dt[0]
def parse(code):
	code = ap(code,';').replace('\\c','\\;')
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
					#for n,v in gvar.items():
					#	if not n in var:
					#		var[n] = v
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
				od = d['atcd']
				oa = d['atc']
				oda = d['atcdat']
				d['atcd'] = ''
				d['atc'] = null
				d['atcdat'] = []
				oa(od[::-1].replace(';','',1)[::-1],oda,line)
			else:
				d['atcd'] += line+';'
def uncompile(cc):
	cc = le(str(cc))
	'''if d['ecnt'] == 0:
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
'''
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
	parser.add_argument('-w', action='store_true')
	parser.add_argument('--warning', action='store_true')
	parser.add_argument('--bddir', type=str)
	parser.add_argument('extra',nargs='*')
	args = parser.parse_args()
	if asu:
		# Auto Setup
		if args.bddir:
			su(args.bddir)
		else:
			su()
	if args.p or args.pyparse:
		d['pyparse'] = True
	if args.pp or args.globalpyparse:
		d['gp'] = True
	if args.w or args.warning:
		d['ignorewarnings'] = True
	if not args.a and not args.autoexec:
		gvar['@fn'] = {'type':'string','dt':bddir+'/pref/autoexec.bd','headers':{}}
		gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
		gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
		gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
		d['filename'] = bddir+'/pref/autoexec.bd'
		d['extraargs'] = args.extra
		with open(bddir+'/pref/autoexec.bd') as data:
			parse(data.read())
	if not args.c:
		if args.filename:
			fn = args.filename
			d['cnt'] = 0
			gvar['@fn'] = {'type':'string','dt':str(Path(fn).absolute()).replace('\\','/'),'headers':{}}
			d['filename'] = str(Path(fn).absolute()).replace('\\','/')
			parse(open(fn).read())
		else:
			d['cnt'] = 0
			print(f'Bird Programming Language {d["version"]}\nCopyright (C) 2022\nType \'writeout(@license)\' to see license.')
			gvar['@fn'] = {'type':'string','dt':'<input>','headers':{}}
			d['filename'] = '<input>'
			parse(console())
	else:
		fn = args.filename
		d['cnt'] = 0
		gvar['@fn'] = {'type':'string','dt':str(Path(fn).absolute()).replace('\\','/'),'headers':{}}
		d['filename'] = str(Path(fn).absolute()).replace('\\','/')
		uncompile(open(fn).read())
def replit(asu=True):
	if asu:
		su()
	print(f'Bird Programming Language {d["version"]}\nCopyright (C) 2022')
	fn = input('Filename: ')
	d['filename'] = fn
	gvar['@fn'] = {'type':'string','dt':str(Path(fn).absolute()).replace('\\','/'),'headers':{}}
	gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
	gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
	gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
	with open(bddir+'/pref/autoexec.bd') as data:
		parse(data.read())
	d['cnt'] = 0
	chdir('tests/')
	parse(open(fn).read())
