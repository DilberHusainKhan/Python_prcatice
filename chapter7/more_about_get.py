user = {
    'name': 'Dilber Husain Khan',
    'age': 23
}
# to print  NOT FOUND instead of none
print(user.get('names','NOT FOUND'))
print(user.get('name','NOT FOUND'))

# if we have more then one same keys in the dictionary then last value will be overide other
user1 ={
    'name': 'Dilber Husain Khan',
    'age': 23,
    'age':32,
}
user2 ={
    'name': 'Dilber Husain Khan',
    'age': 23,
    'age':32,
    'name': 'Humayun Anwar Khan'
}
print(user1)
print(user2)