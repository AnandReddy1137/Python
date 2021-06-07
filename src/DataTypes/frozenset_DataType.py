print('''
It is exactly same as set except that it is immutable.
Hence we cannot use add or remove functions.
''')

s={10,20,30,40}
fs=frozenset(s)
print(fs)
#for i in fs:print(i) // Reading...

print("#fs.add(70)  AttributeError: 'frozenset' object has no attribute 'add'")
print("#fs.remove(10)  AttributeError: 'frozenset' object has no attribute 'remove'")