def equilibrium_index(A):
    totalsum=sum(A)
    leftsum=0
    for i in range(len(A)):
        totalsum-=A[i]
        if leftsum==totalsum:
            return i
        leftsum+=A[i]
    return -1
A=list(map(int,input().split()))
print(equilibrium_index(A))
