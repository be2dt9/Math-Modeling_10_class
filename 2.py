def prod(A):
    s = 1
    for i in range(0,len(A),1):
        s = s*A[i]
        print(s)
    print('----')
    return s

N = [1, 3, 5]
print(prod(N))        