from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    x=s.split(".")
    print(x)
    def fn1(x,y):
        return x*10+y
    def fn2(x,y):
        return x*0.1+y
    def char2num(s):
        return DIGITS[s]
    
    if len(x)>1:
        return reduce(fn1,map(char2num,x[0])) + 0.1*reduce(fn2,map(char2num,x[1][::-1]))
    else:
        return reduce(fn1,map(char2num,x[0]))

print('str2float(\'0.12\') =', str2float('0.12'))
    

