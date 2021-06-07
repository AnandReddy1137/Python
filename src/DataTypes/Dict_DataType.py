print(''' Dic type for key-valued pairs
1.Key value pairs
2.duplicate keys are not allowed but duplicate values are allowed
3.Growable
4.MUTABLE
''')

d={101:'ram',102:'ravi',103:'shiva'}
print("dict:",d)
d[101]='sunny'
print("d[101]='sunny':",d)
d['a']='apple'
print("d['a']='apple'",d)

print(d.popitem()) #remove an element and returns it
print(d.pop(101)) #specify the key, to remove a k-v pair , returns the removed value
#d2=d.copy() for copying the dict