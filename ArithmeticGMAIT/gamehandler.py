import math
import random
import evaluator as evl
import statistics as st
import cmath
#import circuit_analyze as circ

'''
The output of each function is as follows : 
[resulting_string, expected_result, conversion_functon]
'''

def regMulDig(inpt_dict):
    digits = inpt_dict["ndigits"]
    n1 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n2 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n1s = ' '.join([i for i in str(n1)])
    n2s = ' '.join([i for i in str(n2)])
    string = "  %s\n* %s\n"%(n1s, n2s) + ''.join(['-' for i in range(max(len(n1s), len(n2s)) + 2)]) + '\n'
    return [string, n1 * n2, lambda x : int(x)]

def divgame(inpt_dict):
    digits = inpt_dict['ndigits']
    out = inpt_dict['out']
    n1 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n2 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n1s = ' '.join([i for i in str(n1)])
    n2s = ' '.join([i for i in str(n2)])
    string = "%s\n"%n1s + ''.join(['-' for i in range(max(len(n1s), len(n2s)))]) + "\n%s\n"%n2s+ '\n'
    return [string, int((n1 / n2) * 10 ** out) / 10 ** out, lambda x : float(x)]


def arithmetic_elems(ndig, n, cmplx=False, sq=True):
    result = random.randint(0, 10) + random.random()
    result = int(result * 10 ** ndig) / (10 ** ndig)
    curr_str = str(result)
    res_str = str(result)
    MAX = 5 if sq else 4
    c = 0
    for i in range(n):
        op = random.randint(1, MAX)
        while op == 4 and c > 0:
            op = random.randint(1, MAX)
        n2 = random.randint(0, 10) + random.random()
        n2 = int(n2 * 10 ** ndig) / (10 ** ndig)
        if cmplx:
            m2 = random.randint(0, 10) + random.random()
            m2 = int(m2 * 10 ** ndig) / (10 ** ndig)
            n2 = complex(n2, m2)
            
        while n2 == 0:
            n2 = random.randint(0, 10) + random.random()
            n2 = int(n2 * 10 ** ndig) / (10 ** ndig)
            if cmplx:
                m2 = random.randint(0, 10) + random.random()
                m2 = int(m2 * 10 ** ndig) / (10 ** ndig)
                n2 = complex(n2, m2)
    
        if op == 1: # +
            curr_str = (curr_str[:] + "+" + str(n2))[:]
            res_str = (res_str[:] + "+" + str(n2))[:]
            result += n2
        
        elif op == 2: # -
            curr_str = (curr_str[:] + "-" + str(n2))[:]
            res_str = (res_str[:] + "-" + str(n2))[:]
            result -= n2
        
        elif op == 3: # *
            curr_str = ( curr_str[:] + "*" + str(n2))[:]
            res_str = (res_str[:] + "*" + str(n2))[:]
            result *= n2
        
        elif op == 4: # /
            l = max(len(curr_str), len(str(n2)))
            k = min(len(curr_str), len(str(n2)))
            curr_str = curr_str + "\n" + "".join(['-' for j in range(l)]) + "\n"+ "".join([" " for j in range(int((abs(l - k)) / 2)-1)]) + str(n2)
            res_str = ("(" + res_str[:] + ")" + "/" + "(" +str(n2))[:]
            c += 1
        
        elif op == 5:
            nop = random.randint(1, 4)
            while nop == 4 and c > 0:
                nop = random.randint(1, 5)
            nstr = 'sqrt(%s)'%str(n2)
            n2 = cmath.sqrt(n2)
            if nop == 1: # +
                curr_str = (curr_str[:] + "+" + nstr)[:]
                res_str = (res_str[:] + "+" + nstr)[:]
                result += n2
        
            elif nop == 2: # -
                curr_str = (curr_str[:] + "-" + nstr)[:]
                res_str = (res_str[:] + "-" + nstr)[:]
                result -= n2
            
            elif nop == 3: # *
                curr_str = ( curr_str[:] + "*" + nstr)[:]
                res_str = (res_str[:] + "*" + nstr)[:]
                result *= n2
            
            elif nop == 4: # /
                l = max(len(curr_str), len(nstr))
                k = min(len(curr_str), len(nstr))
                curr_str = curr_str + "\n" + "".join(['-' for j in range(l)]) + "\n"+ "".join([" " for j in range(int((abs(l - k)) / 2)-1)]) + nstr
                res_str = ("(" + res_str[:] + ")" + "/" + "(" +nstr)[:]
                c += 1
        
    for i in range(c):
        res_str = res_str + ")"

    return curr_str, evl.evalBcmplx(evl.ins_star(res_str))



def funcEval(inpt_dict):
    ndigits = inpt_dict["ndigits"]
    dig = inpt_dict["dig"]
    
    funcs = ['sin', 'cos', 'exp', 'tan', 'log']
    f = [math.sin, math.cos, math.exp, math.tan, math.log]
    ind = random.randint(0, len(funcs) - 1)
    x = str(random.randint(0, 1) + random.random())[:ndigits+2]
    s = funcs[ind] + '(' + x + ')'
    res = int(f[ind](float(x)) * 10 ** dig) / 10**dig

    return s + ' = ', res, lambda x : float(x)


def arithmetic_game(inpt_dict):
    numdigs = inpt_dict['ndig']
    n = inpt_dict['n']
    ndigits = inpt_dict['ndigits']
    sq = inpt_dict['sq']
    cmplx = inpt_dict['cmplx']
    
    a, b = arithmetic_elems(numdigs, n, cmplx=cmplx, sq = sq)
    if not isinstance(b, complex):
        bres = int(b * 10**ndigits) / (10**ndigits)
    else:
        bres = complex(int(b.real * 10**ndigits) / (10**ndigits), int(b.imag * 10**ndigits) / (10**ndigits))
    return a + "\n > ", bres, lambda x : complex(x)


def complex_mult_game(inpt_dict):
    ndigits = inpt_dict['ndigits']
    n1 = complex(random.randint(10**(ndigits-1), 10**(ndigits) - 1), random.randint(10**(ndigits-1), 10**(ndigits) - 1))
    n2 = complex(random.randint(10**(ndigits-1), 10**(ndigits) - 1), random.randint(10**(ndigits-1), 10**(ndigits) - 1))
    st = "%s%s = "%(str(n1), str(n2))
    res = n1 * n2
    check_method = lambda x : complex(x)
    return st, res, check_method

def trachtenberg(inpt_dict):
    digits = inpt_dict["ndigits"]
    n1 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n2 = random.randint(10 ** (digits - 1), 10 ** (digits) - 1) 
    n1s = ' '.join([i for i in str(n1)])
    n2s = ' '.join([i for i in str(n2)])
    string = "  %s\n* %s\n"%(n1s, n2s) + ''.join(['-' for i in range(max(len(n1s), len(n2s)) + 2)]) + '\n'
    return [string, str(n1 * n2)[::-1], lambda x : x]