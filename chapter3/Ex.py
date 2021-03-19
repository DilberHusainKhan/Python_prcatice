import random
import math

number = math.floor(random.randint(0,9))
guess_number = int(input("Enter guess number 0-9 \t"))
if number == guess_number:
    print("You won ")
else:
    print(f"you lose {number}")
# ////////////////////////////////////////
city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Random element from list:", random.choice(city_list))
    

