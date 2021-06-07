print('''
range Data Type represents a sequence of numbers
''')

r=range(10) # 0 to 9
print('r=range(10)')
for i in r : print(i)

range(10,20) #10 to 19

range(10,20,2) #10,12,14,16,18
print(" #r[15]==>IndexError: range object index out of range")

print("#r[0]=100 TypeError: 'range' object does not support item assignment")
