from os import chdir
from src.bird import *
fn = input('Filename: ')
gvar['@fn'] = {'type':'string','dt':"autoexec.bd",'headers':{}}
parse(open('Bird/pref/autoexec.bd').read())
d['cnt'] = 0
chdir('tests/')
gvar['@fn'] = {'type':'string','dt':fn,'headers':{}}
parse(open(fn).read())