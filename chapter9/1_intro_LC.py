# List Comprehension
# with the help of the list Comprehension , we can create list in  one line.

###################### EX1- to Create a list of square from 1 to 10:##############################
# NORMAL WAY
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares) 

# LIST COMPREHENSION TECH
squares1 = [i**2 for i in range(1,11)]
print(f"by list comprehension tech {squares1}.")

# ####################### EX2- To store negative number in the list from 1 to 10##################
# NORMAL WAY
negativeNo =[]
for i in range(1,11):
    negativeNo.append(-i)
print(negativeNo)

# LIST COMPREHENSION WAY
negative_NO = [-i for i in range(1,11)]
print(negative_NO)

###########################EX3- to store first letter of string stored in the list name to a new list#########
# BASIC WAY
names = ['Dilber', 'Husain','Khan']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)

# LIST COMPREHENSION WAY
new_list1 = [name[0] for name in names]
print(new_list1)

