from functools import reduce
import pdb

def str2num(s):
    #捕获可能出现的类型错误
    try:
        x=int(s)
        return x
    except ValueError as e:
        print('ValueError')
        return float(s)


    

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
print('END')
