def Insertion_sort(A):
    for i in range(1,len(A)):
        sel=i
        while(A[sel] < A[sel-1] and sel >=1):
            swap(A,sel,sel-1)
            sel=sel-1

def swap(A,x,y):
    A[x],A[y]=A[y],A[x]

A=[1,5,8,3,5,6,9,3,0]

Insertion_sort(A)

print(A)