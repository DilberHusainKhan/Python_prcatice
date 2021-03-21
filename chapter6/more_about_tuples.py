# looping in tuples
# tuple with one element
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples


mixed = (1,2,3,4.0)
# print(mixed)

# for loop in tuple
# for i in mixed:
#     print(i)
# -----------------*****---------------------
# while loop in tuple

# i=0
# while i< len(mixed):
#     print(mixed[i])
#     i+=1

# Tuple with one elemnt
num = (1)
# print(type(num))  # <class 'int'>
num1 = (1,)
# print(type(num1))  #<class 'tuple'>
word=('words')
word1 =('words',)
# print(type(word))  # <class 'str'>
# print(type(word1)) # <class 'tuple'>

# tuple without parenthesis
guitar = 'yamaha' ,'baton rouge', 'taylor'
# print(type(guitar)) # <class 'tuple'>

# tuple unpacking 
# {before unpacking we must know that numnber of variable should besame as number of element in the tuple}
# else we get error 
# name = ('Dilber', 'Husain', 'Khan')
# name1, name2, name3 =(name)
# print(name1)

# list inside tuples
name = ('Darab Ahmed Khan',['Dilber Husain Khan', 'Mhod Aadil Rana', 'Javvad Khan'])
name[1].pop()
name[1].append('Abdullah')
print(name)


# Some funtion we used in the tuple
# min(), max(), sum

print(min(mixed))
print(max(mixed))
print(sum(mixed))