print('''---------------------------------------------------
We can represent int values in the following ways
1. Decimal form
2. Binary form
3. Octal form
4. Hexa decimal form
---------------------------------------------------
''')
a=10
print("1. Decimal form a= 10 ")

a = 0B1111
b =0B1001
c=0b1110
print("2. Binary form a = 0B1111 : {0},\t b =0B1001 : {1} , \t c=0b1110 {2}:".format( a,b,c))

a=0o123
a=0O231
print("3. Octal  form  a=0o123:{0} ,  \t  a=0O231 : {1}".format( a,b))

a =0XFACE
b=0XBeef
c =0xBee
print("4. Hexadecimal form a =0XFACE :{0} \t  b=0XBeef :{1}  \t c =0xBee :{2}".format( a,b,c))