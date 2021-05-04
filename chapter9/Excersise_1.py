# define a function that take in as a Strings
# list contains reverse of all string
# NOTE - Use LIST COMPREHENSION method
# ex 
# l = ['abc', 'tuv', 'xyz'] 
# reverse_string ----> ['cba','vut','zyx']
l = []
def inputString():
    l = input("Enter list name and seprated by comma ").split(',') 
    return l
l = inputString()

reverse_string = [name[::-1] for name in l]

print(reverse_string)