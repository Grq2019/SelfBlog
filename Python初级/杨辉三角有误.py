def triangles():
    L=[1]
    yield L
    while True:
        M=list(L)
        i=1
        while i<len(M):
            L[i]=M[i-1]+M[i]
            i=i+1
        L.append(1)
        yield L

n = 0
results = []
for t in triangles():
    results.append(t)
    if n>0:
        print(results[n-1])
    n = n + 1
    if n == 10:
        break
print(results[8])