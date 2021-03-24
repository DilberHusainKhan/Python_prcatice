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

#To Add key value in dictionary
user_info['Technical_skill'] = ['C','C++','Python','Java','Flutter']

# POP METHOD
# pop method will delete the item on the bases of key 
# and return the value of deleted item & you must pass altest one variable in pop method

poped_item = user_info.pop('education')
print(f"Poped item is {poped_item}")
print(type(poped_item))


# popitem method
# it delete any ramdom value in the dictionary

pop_by_item_method = user_info.popitem()

print(f"Poped item by item method {pop_by_item_method}")
print(type(pop_by_item_method))





print(user_info)