# formkeys
d = {'name': 'unknown', 'age': 'unknown'}
print(d)
a = dict.fromkeys(['name','age','height'],'unknown')
print(a)
b = dict.fromkeys(('name','age','height'),'unknown')
c = dict.fromkeys("DILBER",'unknown')
d = dict.fromkeys(range(1,11),'unknown')
print(b)
print(c)
print(d)
e = dict.fromkeys(['name','age','height'], ['DILBER', 'HUSAIN'])
print(e)