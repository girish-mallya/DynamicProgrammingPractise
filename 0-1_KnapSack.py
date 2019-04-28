'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val)-1
#print(n)

#without DP
def KS(n,W):
    if n==0 or W==0:
        return 0
    elif wt[n]>W:
        KS(n-1,W)
        

    else:
        temp1=KS(n-1,W)
        temp2=val[n] + KS(n-1, W-wt[n])
        return(max(temp1,temp2))
    
print(KS(n,W))

myKS=[[None for x in range(0,W+1)] for x in range(0,n+2)]

print(len(myKS[0]))

def KS2(n,W):
    #print(n,W)
    if myKS[n][W] is not None:
        return myKS[n][W]
    if n==0 or W==0:
        return 0
    elif wt[n]>W:
        KS2(n-1,W)
        
    else:
        temp1=KS2(n-1,W)
        temp2=val[n]+ KS(n-1, W-wt[n])
        myKS[n][W]=max(temp1,temp2)
        return myKS[n][W]
    
print(KS2(n,W))
#print(myKS)

        
