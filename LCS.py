X = "AGGTAB"
Y = "GXTXAYB"
m=len(X)
n=len(Y)

#print(m,n)

L = [[None]*(n+1) for i in range(m+1)] 

#print(len(L),len(L[0]))

def LCS(X,Y,m,n):
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        return (1+LCS(X,Y,m-1,n-1))
    else:
        temp1=LCS(X,Y,m-1,n)
        temp2=LCS(X,Y,m,n-1)
        return (max(temp1,temp2))


z=LCS(X,Y,m,n)
print(z)

#print(L)
def LCS2(X,Y,m,n):
    #print(m,n)
    if L[m][n] is not None:
        return L[m][n]
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        res= 1+LCS(X,Y,m-1,n-1)
    else:
        temp1=LCS(X,Y,m-1,n)
        temp2=LCS(X,Y,m,n-1)
        res=max(temp1,temp2)
    L[m][n]=res
    return L[m][n]
    
z=LCS2(X,Y,m,n)
print(z)
