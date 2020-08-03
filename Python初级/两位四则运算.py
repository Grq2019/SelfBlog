while(input("请输入 'e' to exit and 'c' to continue  ")!='e'):
    x=int(input('x='))
    sign=input()
    y=int(input('y='))
    if sign=='*':
        print(x,sign,y,'=',x*y)
    elif sign=='/':
        print(x,sign,y,'=',x/y)
    elif sign=='+':
        print(x,sign,y,'=',x+y)
    elif sign=='-':
        print(x,sign,y,'=',x-y)


