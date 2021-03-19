import random

win_number = random.randint(1,100)
guess = 1

# while True:
#     guess_number = int(input("Enter number bertween 1 to 100:- "))
#     if guess_number == win_number:
#         print(f"You win , and you guess this in {guess} times ")
#         break
#     else:
#         if guess_number< win_number:
#             print("too low")
#         else:
#             print("too high")
#         guess +=1
#         continue

# Both are same


guess_number = int(input("Enter number bertween 1 to 100:- "))
game_over = False
while not game_over:
    if guess_number == win_number:
        print(f"You win , and you guess this in {guess} times ")
        game_over = True
    else:
        if guess_number< win_number:
            print("too low")
        else:
            print("too high")
        guess +=1
        guess_number =int(input("Enter again "))