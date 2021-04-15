# program to store data form user in dictionary


user = {}
name = input("Enter you name \n")
age = int(input("Enter your age \n"))
fav_song = input("Enter fav songs seprated by , \n").split(',')
fav_movie = input("Enter fav movies seprated by , \n").split(',')
  
user['name'] = name
user['age'] = age
user['fav_song'] = fav_song
user['fav_movie'] = fav_movie

# print(user)

# using for loop key , value 
for key , value in user.items():
    print(f"{key} : {value} ") 



