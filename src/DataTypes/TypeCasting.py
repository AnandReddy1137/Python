print("Type casting using int()")
print('''---------------------------------------------
1. We can convert from any type to int except complex type.
2. If we want to convert str type to int type, compulsary str should contain only integral 
value and should be specified in base-10
---------------------------------------------''')

print("int(123.987):" ,int(123.987) )
print("int(10+5j) : TypeError: can't convert complex to int" )
print("int(True):" ,int(True) )
print('int("10.5") : ValueError: invalid literal for int() with base 10: "10.5"')
print("int(10.5):", int(10.5))
print("int(0b1011):", int(0b1011))


print("\nType casting using float():")
print('''---------------------------------------------
1. We can convert any type value to float type except complex type.
2. Whenever we are trying to convert str type to float type compulsary str should be 
either integral or floating point literal and should be specified only in base-10.
---------------------------------------------''')

print("float(123):" ,float(123) )
print("float(10+5j) : TypeError: can't convert complex to float" )
print("float(True):" ,float(True) )
print('float("10") :', float("10"))
print("float(10):", float(10))
print("float(0b1011):", float(0b1011))


print("\nType casting using complex():")
print('''---------------------------------------------
Form1: complex(x)
We can use this function to convert x into complex number with real part x and imaginary part 0
---------------------------------------------''')

print("complex(123):" ,complex(123) )
print("complex(True):" ,complex(True) )
print('complex("10") :', complex("10"))
print('complex("10.5") :', complex("10.5"))
print("float(10):", float(10))
print("float(0b1011):", float(0b1011))


print("\nForm 2: complex(x,y)")

print(" complex(10,-2)",complex(10,-2))
print("complex(True,False)=",complex(True,False))


print("\nType casting using str():")
print('''---------------------------------------------
''')

print("str(123):" ,str(123) )
print("str(10+5j) :", str(10+5j))
print("str(True):" ,str(True) )
print("str(10.5):", str(10.5))
print("str(0b1011):", str(0b1011))