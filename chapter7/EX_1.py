# Excersise
# define a function that takes a number(n)
# return a dictionary contain cube of number from 1 TO n.
# Cube_finder(n)
# {1:1, 2:8, 3:27}
def Cube_finder(n):
    cube = {}
    for i in range(1 , n+1):
        cube[i] = i**3
    return cube

n= int(input())
print(Cube_finder(n))