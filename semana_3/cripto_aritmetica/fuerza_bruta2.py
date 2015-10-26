import string, re, itertools, time

import sys

if sys.version[0]=='2':
    maketrans = string.maketrans
else:
    maketrans = str.maketrans

def faster_solve(formula):
    """Dada una formula como 'ODD + ODD == EVEN', encontrar los
    digitos que puedan resolverla.
    entrada: formula es una cadena;
    salida: es una cadena de con los digitos que son correctos"""
    f, letters = compile_formula(formula)
    l = []
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = maketrans(letters, ''.join(map(str, digits)))
                l.append(formula.translate(table))
        except ArithmeticError:
            pass
    print("%d SOLUCIONES ENCONTRADAS PARA LA FORMULA"%(len(l)))
    if(len(l))>0:
        print("ej. %s"%(l[0]))
    return l

def compile_formula(formula, verbose=False):
    """ Compila la formula en una funcion. Tambien retorna las letras encontradas en un str
    en el mismo orden que los parametros de la funcion. Por ejemplo
        compile_formula('YOU == ME**2') returna
    (lambda Y, M, E, U, O): (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

def compile_word(word):
    """Compila una palabra en MAYUSCULA como digitos numericos.
    Ej. compile_word('YOU') returns '(1*U+10*O+100*Y)'
    Palabras en minuscula se mantienen igual: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

examples = """TWO + TWO == FOUR
GLITTERS is not GOLD
ATOM**0.5 == A + TO + M
""".splitlines()

def test():
    t0 = time.time()
    for example in examples:
        print('\n '+13*' '+str(example))
        print('%6.4f sec.' % timedcall(faster_solve, example))
    print('%6.4f tot.' % (time.time()-t0))

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1-t0

test()
