n = int(input())
a=""
b=""
A=[]
B=[]
C=[]
for i in range(n):
    a,b = input().split()
    b = float(b)
    A.append(a)
    B.append(b)
    C.append(b)
B.sort(reverse=True)
for i in range(n):
    print(A[i],B.index(C[i])+1)