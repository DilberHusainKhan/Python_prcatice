percentage = int(input("Enter your percentage "))
if percentage<=35:
    print("You are failed")
    # elif 35<percentage<=75:
elif percentage>35 and percentage<=75:                
    print("passed")
else:
    print("passed with distintion")


age= int(input("Enter your age "))


if age<=0:
    print("Invalid input")
else:
    if 0<age<3:
        print("free ")
    elif 3<age<=10:
        print(" Rs. 150")
    elif 10<age<=60:
        print("Rs. 250")
    else:
        print("Rs. 200")