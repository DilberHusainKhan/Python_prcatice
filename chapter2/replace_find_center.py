name = "Imdad Husain Khan"
print(name.replace("H","_"))


st = "she is beautiful and she is also cute is"
print(st.replace("is","was"))
print(st.replace("is","was",2))

# ***********    find  *******************//
print(st.find("is"))
print(st.find("is",6))

# ///////////////   center    /////////////////

name1 = input("Enter your name")
print(name1.strip().center(len(name1.strip())+8,"*"))