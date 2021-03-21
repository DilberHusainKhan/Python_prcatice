#define a function which will take list containing number as input 
# and rturn list containing square of every elements

def sq_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

number = list(range(1,6))
print(number)
print(sq_list(number))