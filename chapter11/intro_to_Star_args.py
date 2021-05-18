# make flexible function
# *Operator
# *args
# Let we have a function 
def total(a,b):
    return a+b
# print(total(3,4,10,9))  #TypeError: total() takes 2 positional arguments but 4 were given

#   To solve this error we will use *args
def all_total(*args):
    # 1,2,3,4,5,6,7,89,9
    total = 0
    for num in args:
        total +=num
    return total
print(all_total(1,2,3,4,5,6,7,89,9))

# To multiply the number with * args
def multiply_num(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_num(2,3,4))
