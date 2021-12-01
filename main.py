from os import chdir
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
parse(open(fn).read())
'''gvar['@fn'] = {'type':'string','dt':''}
var['dt'] = {'type':'class','dt':{'z':{'type':'string','dt':'v'}}}
var['cls'] = {'type':'class','dt':{}}
var = clsrec(['cls','a'],{'type':'string','dt':'test'},var)
var = clsrec(['cls','z'],{'type':'number','dt':1},var)
parse('using("stdio.bd");writeout(cls.a);writeout(cls.z)');'''