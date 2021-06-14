print("""
This program is understand the pythons behaviour with the function's containing list and Dict datatype
""")

print("Example:1 list/dict as function parameter")

def m1(A):
#    A[len(A)-1]=10 #or use A.append(10)
    A.append(3)
    print("inside m1:",A)

A=[1,2]
print("before the m1(): ",A)
m1(A)
print("After the m1(): ",A)

print('''
If you observe the value of A itself is changed (this is similar for list and Dic)
''')

print('''
Eacmple:2 int/float/complex as function parameter''')

def f2(B):
    B=B*2
    print("value in fnct",B)

B=20
print("before the f2(): ",B)
f2(B)
print("After the f2(): ",B)
print("Value of B changed only in the function, after coming out of it, its values is still same as orginal")

print('''
Why such kind of difference with list/dict and other data types?
list/Dic are mutable, where all the other datatype(int/float/tuple.... are immutable.

So the list/Dict parameters works a pass-by-reference.

''')