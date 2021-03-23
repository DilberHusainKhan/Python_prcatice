# user_info dictionary 
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

# 3.1 to check key present in dictionary
if 'name' in user_info:
    print(user_info['name'])
else:
    print('key is not present')

#3.2 To check if value exist in dictionary
if 24 in user_info.values():
    print(user_info.keys())
else:
    print("Value is not present")
#3.3 To check complete list is present in dictionary or not.
if ['Dilber','Husain','Khan'] in user_info.values():
    print(user_info)
    # print(user_info.items())
else:
    print('Not Present')

###3.4 Loop in dictionary
# ***TO Print Keys in the dictionary
for i in user_info:
    print(i)

print("***To print values of the Dictionary")
for i in user_info.values():
    print(i)
    #OR 
for i in user_info:
    print(user_info[i]) 

#3.5 VALUES METHOD {values()}
val_values = user_info.values()
print(val_values)
print(type(val_values)) #type of this val is dictionary


#3.6 KEYS METHOD {keys()}
val_key = user_info.keys()
print(val_key)
print(type(val_key))

# 3.7 ITEMS METHOD {items()}

user_item = user_info.items()
print(user_item)
print(type(user_item))

# Why item is important  
for key , value in user_info.items():
     print(f'Key is {key} and value is {value}')

for i,j in user_info.items():
    print(f'Key of user is {i} and value is {j}')