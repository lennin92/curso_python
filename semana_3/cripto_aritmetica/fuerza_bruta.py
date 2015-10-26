import string, re, itertools, time

import sys

if sys.version[0]=='2':
    maketrans = string.maketrans
else:
    maketrans = str.maketrans
    
def valid(f):
    "debe evaluar la cadena"
    pass
        
def fill_in(formula):
    "generar todas las formulas posibles de las letras con digitos"
    letters = ''.join(set(re.findall('[A-Z]', formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = maketrans(letters, ''.join(digits))
        yield formula.translate(table)
        
def solve(formula):
    """Dada una formula como 'ODD + ODD == EVEN', encontrar los 
    digitos que puedan resolverla.
    entrada: formula es una cadena; 
    salida: es una cadena de con los digitos que son correctos"""
    l = []
    # ENCONTRAR TODAS LOS VALORES REALES
    print("%d SOLUCIONES ENCONTRADAS PARA LA FORMULA"%(len(l)))
    if(len(l))>0:
        print("ej. %s"%(l[0]))
    return l
            
examples = """TWO + TWO == FOUR
GLITTERS is not GOLD
ATOM**0.5 == A + TO + M
""".splitlines()

def test():
    t0 = time.time()
    for example in examples:
        print('\n '+13*' '+str(example))
        print('%6.4f sec.' % timedcall(solve, example))
    print('%6.4f tot.' % (time.time()-t0))

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1-t0

test()
