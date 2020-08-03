def is_palindrome(n):
    L=[]
    while n !=0 :
        s=n%10
        L.append(s)
        n=n//10
    for i in range(0,len(L)//2):
        if L[i] != L[-i-1]:
            return False
    return True
    
output = filter(is_palindrome, [100,93539,1059501])
print('1~1000:', list(output))
