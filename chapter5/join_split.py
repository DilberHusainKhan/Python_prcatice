
#Split method
#Convert String to list
user_info = "DIlber 35 56 78"
print(user_info)
user_info1= user_info.split()
print(user_info1)
name, age, English_marks, Hindi_marks =user_info.split()
print(name) 
print(age) 
print(English_marks) 
print(Hindi_marks) 

user_in = "DIlber,35,56,78".split(',')
print(user_in)

#Join method
#Conver list to String
userinfn = ["Dilber Husain", "23"] # all elements must be in string
print(" ".join(userinfn)) # " " you can pass anything in the " " it repeat after every string.  

