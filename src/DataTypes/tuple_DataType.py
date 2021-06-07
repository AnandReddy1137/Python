print(''' tuple is IMMUTABLE ()
1. insertion order is preserved
2. heterogeneous objects are allowed
3. duplicates are allowed
''')

t=(10,20,'python',30,40)
print("t=(10,20,'python',30,40):",t)

print("------Tuple functions------")
print('# t(0)=11 not supported IMMUTABLE')
print("t.count(10) :",t.count(10))
print("t.index(20) :",t.index(20))
print("t.index('python', 1, 5):",t.index('python', 1, 5))
print("#t.index('python1', 1, 5) //ValueError: tuple.index(x): x not in tuple")