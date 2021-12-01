from os import chdir
import sys
from pathlib import Path
from src.bird import parse,gvar,d #Replace with contents of src.bird!
home = str(Path.home())+'/Bird-Lang' #Only for Replit: +'/Bird-Lang'
bddir = open(home+'/bddir.txt').read()
gvar['@fn'] = {'type':'string','dt':bddir+'/pref/autoexec.bd','headers':{}}
gvar['@version'] = {'type':'string','dt':d['version'],'headers':{}}
gvar['@v'] = {'type':'string','dt':d['version'],'headers':{}}
gvar['@cf'] = {'type':'string','dt':'@main','headers':{}}
gvar['@license'] = {'type':'string','dt':open('LICENSE').read(),'headers':{}}
with open(bddir+'/pref/autoexec.bd') as data:
	parse(data.read())
def console():
	code = input('>>> ')
	ll = code
	while True:
		ic = input('... ')
		if ic == '':
			return code
		elif ic == 'rewrite_lastline':
			code = code[::-1].replace(ll[::-1],'',1)[::-1]
		elif ic == 'rll':
			code = code[::-1].replace(ll[::-1],'',1)[::-1]
		else:
			ll = ic
			code += ic
if len(sys.argv) >= 2:
	fn = sys.argv[1]
	d['cnt'] = 0
	gvar['@fn'] = {'type':'string','dt':fn,'headers':{}}
	chdir('tests/')
	parse(open(fn).read())
else:
	d['cnt'] = 0
	print(f'Bird Programming Language {d["version"]}\nCopyright (C) 2021\nType \'writeout(@license)\' to see license.')
	gvar['@fn'] = {'type':'string','dt':'<input>','headers':{}}
	parse(console())