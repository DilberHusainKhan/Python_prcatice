# map function 
number = [1,2,3,4,5]

def square(a):
    return a**2

square = lambda a: a**2
squares = list(map(square,number))
print(squares)
# map function using lambda expression
print(list(map(lambda a:a**2, number)))

# List comprehension 
squar=[a**2 for a in number]
print(squar) 

# Square without LC, MAP 
new_list = []
print("Square without LC, MAP ")
for i in number:
    new_list.append(square(i))    
print(new_list)

# TO print the length of string in a list 
Name = ['abc', 'abcd','efghi','jklmnn']
length = map(len ,Name)
print(f"{[name for name in Name]} ----> {[i for i in length]}")