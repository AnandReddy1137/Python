print(''' set is MUTABLE
1. insertion order is not preserved
2. duplicates are not allowed
3. heterogeneous objects are allowed
4. index concept is not applicable
5. It is mutable collection
6. Growable in nature
''')

s={100,0.5,10,200,10,'python'}
print("s={100,0.5,10,200,10,'durga'} \n s:",s)

print("#s[0] ==>TypeError: 'set' object does not support indexing ")

s.add(199.99)
print("s.add(199.99) s:",s)
s2=s.copy()
print("s2=s.copy() s2:",s2)
print("#pop() removes a element , returns it")
p=s.pop()
print("p=s.pop() s:",s)
print("p:",p)
s.remove(10)
print("s.remove(10) s:",s)
print("#remove(x) removes x if there else return the wholes set")