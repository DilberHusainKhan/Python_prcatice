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

# GET menthod (useful)
name = {
    'first': 'Humayun',
    'middle': 'Anwar',
    'last': 'Khan'
}

print(name['first'])
# print(name['middle name'] #print error if key is not found
print(name.get('first name')) # print none if key is not found

if 'first' in name:
    print('key is Present')
else:
    print('Key ks not present')

# OR
if name.get('first name'):
    print("Present")
else:
    print("key is not present") 

# Clear method
# name.clear() # it delete the dictionary
print(name)

# Copy method
n = name.copy()
print(n)

# if we assign n = name the n can also be a new dictionary but 
# it should be same if we delete the item from n then it automatically deleted from name 
m = name
print('------------------------------------------------------------------')
print(m.popitem())
print(m)
print(name)
print(n)