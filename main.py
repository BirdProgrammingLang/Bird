'''from os import chdir
from pathlib import Path
from src.bird import parse,gvar,d
global gvar
print('Bird Programming Language \nCopyright (C) 2021')
fn = input('Filename: ')
home = str(Path.home())+'/Bird-Lang' #Only for Replit: +'/Bird-Lang'
bddir = open(home+'/bddir.txt').read()
gvar['@fn'] = {'type':'string','dt':Path(fn).absolute(),'headers':{}}
gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
gvar['@license'] = {'type':'string','dt':open('LICENSE').read(),'headers':{}}
with open(bddir+'/pref/autoexec.bd') as data:
	parse(data.read())
d['cnt'] = 0
chdir('tests/')
parse(open(fn).read())'''
'''gvar['@fn'] = {'type':'string','dt':''}
var['dt'] = {'type':'class','dt':{'z':{'type':'string','dt':'v'}}}
var['cls'] = {'type':'class','dt':{}}
var = clsrec(['cls','a'],{'type':'string','dt':'test'},var)
var = clsrec(['cls','z'],{'type':'number','dt':1},var)
parse('using("stdio.bd");writeout(cls.a);writeout(cls.z)');'''
#from pathlib import Path
from src.bird import su,replit
su("C:/Users/alexa/Documents/coding/python/bird")
replit(False)
#d = {'using':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'file': ['', ''], 'global': ['bool', 'True', {}], 'compile': ['bool', 'False', {}]}, 'code': 'CNCHEADER6 file;CNCHEADER6 global;CNCHEADER6 compile;CNC6', 'head': {}}}, 'array_item': {'type': 'funct', 'dt': {'attrib': {'arr': ['', ''], 'cnt': ['', '']}, 'code': "\n\tcreate var data 'notdefined';\n\tpyparse `if var['cnt']['type'] == 'number':\n\tvar['cnt']['dt'] = int(var['cnt']['dt'])\nvar['data']['dt'] = var['arr']['dt'][var['cnt']['dt']]['dt']`;\n\treturn data\n", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '','pyparse':'true'}}}, 'eval': {'type': 'funct', 'dt': {'attrib': {'code': ['', '']}, 'code': "pyparse `parse('''@{code}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb','pyparse':'true'}}}, 'quit': {'type': 'funct', 'dt': {'attrib': {'status': ['number', 0.0]}, 'code': 'pyparse `quit(int(@{status}))`', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb'}}}, 'dirsarray': {'dt': {'bird': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/'}, 'lib': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/lib/'}, 'package': {'type': 'string', 'dt': '/home/runner/Bird-Lang/Bird/package/'}}, 'type': 'associative'}, 'fread': {'dt': {'attrib': {'fn': ['', '']}, 'code': 'pyparse `var[\'data\'] = {\'type\':\'string\',\'dt\':open("@{fn}").read()}`;return data', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'}, 'fwrite': {'dt': {'attrib': {'fn': ['', ''], 'txt': ['', ''], 'm': ['string', 'a']}, 'code': 'pyparse `d = open("""@{fn}""","""@{m}""")\nd.write("""@{txt}""")\nd.close()`;return true', 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'}, 'fdelete': {'dt': {'attrib': {'fn': ['', '']}, 'code': "pyparse `import os\nos.remove('''@{fn}''')`", 'head': {'sep': ':', 'scb': '\\scb', 'ecb': '\\ecb', 'global': '', 'pyparse': 'true'}}, 'type': 'funct'},'typeof':{'dt': {'attrib': {'item': ['', '']}, 'code': 'pyparse `var["data"] = {\'type\':\'string\',\'dt\':var[\'item\'][\'type\'],\'headers\':{}}`;return data', 'head': {'global': '', 'pyparse': 'true'}}, 'type': 'funct', 'headers': {}},'streval':{'type': 'funct', 'headers': {}, 'dt': {'attrib': {'string': ['', '']}, 'code': 'pyparse `tdt = typeify(""" @{string} """)\nvar[\'dt\'] = {"type":tdt[0],"dt":tdt[1],"headers":tdt[2]}`;return dt', 'head': {'pyparse': 'true'}}}}
#for item in d.keys():
#	print(item)