# make dictionary
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
print(f"before update {user_info} .")

more_info = {
    'name' : ['Humayun', 'Anwar', 'Khan'],
    'state' : 'Uttar Pradesh',
    'hobbies' : ['Coding', 'Listening Music', 'Cooking']
}

# update() method
user_info.update(more_info)
print(f"After update more_info, name will also update {user_info} .")
user_info.update({}) # blank {} means you will not add any data.
print(user_info)
