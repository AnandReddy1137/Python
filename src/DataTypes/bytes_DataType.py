x = [10,20,30,40]
b = bytes(x)
type(b)
print(b[0])
print(b[-1])
for i in b : print(i)

print(''' 
Conclusion 1: (b=[1,260]  bytes(b) // ValueError: bytes must be in range(0, 256)
The only allowed values for byte data type are 0 to 256. By mistake if we are trying to 
provide any other values then we will get value error.

Conclusion 2: ( b[0]=100 // TypeError: 'bytes' object does not support item assignment )
Once we creates bytes data type value, we cannot change its values,otherwise we will get 
TypeError.
''')