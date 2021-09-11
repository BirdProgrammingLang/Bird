from os import chdir
chdir('tests/')
from src.bird import *
fn = input('Filename: ')
gvar['@fn'] = {'type':'string','dt':fn}
parse(open(fn).read())