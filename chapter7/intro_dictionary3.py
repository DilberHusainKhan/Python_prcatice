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

# to check key present in dictionary
if 'name' in user_info:
    print(user_info['name'])
else:
    print('key is not present')

# To check if value exist in dictionary
if 24 in user_info.values():
    print(user_info.keys())
else:
    print("Value is not present")

