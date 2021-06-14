def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if(A[j]<A[j-1]):
                swap(A,j,j-1)

    return A


def swap(A,x,y):
    A[x],A[y]=A[y],A[x]


if __name__ == '__main__':
    A=['s','r','t','a','h','_','@','#']
    B=[10,50,49,79,20,6]
    bubble_sort(A)
    bubble_sort(B)
    print("Sorted A:",A)
    print("Sorted B:", B)



