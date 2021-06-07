print(''' list is MUTABLE []
1. insertion order is preserved
2. heterogeneous objects are allowed
3. duplicates are allowed
4. Growable in nature
5. values should be enclosed within square brackets.
''')

list=[10,10.5,'python',True,40]
print("list:",list) # [10,10.5,'durga',True,40]
print("list[0]:",list[0]) #10
print("list[-1]:",list[-1]) #40
print("list[1:3]: ",list[1:3]) #[10.5,'python']

print("________List functions_______")

print(list.pop()) #[10, 10.5, 'python', True] last element will be returned removed
print("list.count(10):", list.count(10))

list.append(99)
print("list.append(99):",list)
l2=list.copy()
print("l2=list.copy() l2:",l2)
list.extend([23,32])
print("list.extend([23,32]) list:",list)

list.insert(1,"One")
print('list.insert(1,"One"):',list)

list.remove(10)
print("list.remove(10) :list",list)

list.reverse()
print("list.reverse() :",list)

#list.sort()  not supported between str and int

a=[2,5,6,0]
b=['b','n','uu','a']
a.sort()
b.sort()
print("a.sort()",a)
print("b.sort()",b)