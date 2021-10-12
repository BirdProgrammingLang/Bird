from os import chdir
from src.bird import *
fn = input('Filename: ')
gvar['@fn'] = {'type':'string','dt':"autoexec.bd"}
parse(open('Bird/pref/autoexec.bd').read())
d['cnt'] = 0
chdir('tests/')
gvar['@fn'] = {'type':'string','dt':fn}
parse(open(fn).read())
'''gvar['@fn'] = {'type':'string','dt':''}
var['dt'] = {'type':'class','dt':{'z':{'type':'string','dt':'v'}}}
var['cls'] = {'type':'class','dt':{}}
var = clsrec(['cls','a'],{'type':'string','dt':'test'},var)
var = clsrec(['cls','z'],{'type':'number','dt':1},var)
parse('using("stdio.bd");writeout(cls.a);writeout(cls.z)');'''