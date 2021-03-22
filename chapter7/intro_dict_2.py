# 1 Because of limitation of lists, lists are not enough to represent real data

# give list contain name, age , education, address

user = [['Dilber','Husain','Khan'],24,[10,12,'B.Tech'],'Kaimganj']
# print(user)
# print(user[0][1])
# print(type(user))  

# 2 Dictionaries
# unordered collections of data in  key:value Pair.

#3 how to create dictionaries
#   3.1 way 1 BY {}
user_1 ={'name': 'Humayun Khan', 'age': 24, 'address': 'Kaimganj'}
# print(user_1)
# print(type(user_1))

#   3.2 way 2  (dict method)
user_2 = dict(name = 'Dilber Husain Khan', age = 24)
# print(user_2)
# print(type(user_2))

#4  how to access data from dictionary
# NOTE-There is no indexing because of unordered collection of data.
# print(user_2['name'])

#5 which type of data can be stored?
# anytype
# number , string , list ,dictionary
user_info ={
    'rollnumber':1901320,
    'name': ['Dilber','Husain','Khan'],
    'age':24,
    'education':{
        '10':'CPVN',
        '12': 'CPVN',
        'Diploma': 'Jamia Millia Islamia'
    }
}
print(user_info)
print(user_info['education']['Diploma'])

#6 how to add data into a empty dictionary
user_info2={}
user_info2['name']=['Dilber','Husain','Khan']
user_info2['age'] =24
print(user_info2)

# 7 TO CHECK IF KEY IS PRESENT IN DICTIONARY
if 'name' in user_info:
    print('Present')
    print(user_info['name'])
else:
    print('absent')