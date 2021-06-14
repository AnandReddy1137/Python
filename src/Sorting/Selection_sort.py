def selection_sort(A):
    for i in range(len(A)):
        least=i
        for k in range(i+1,len(A)):
            if(A[least]>A[k]):
                least=k
        swap(A,i,least)

def swap(A,a,b):
    A[a],A[b]=A[b],A[a]

A=[1,5,4,2,8,2,0,3]
B=['s','r','t','a','h','_','@','#']  #// output: ['#', '@', '_', 'a', 'h', 'r', 's', 't']

print(A)
selection_sort(A)
print('Sorted',A)

print(B)
selection_sort(B)
print('Sorted',B)