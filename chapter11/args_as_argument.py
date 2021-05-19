def multiply_num(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

num = [2,3,4,5]
print(multiply_num(num)) # If we use argument without * args treat as a single argument like list, tuple, and etc. 
# OUTPUT ([2,3,4,5],)
# [2,3,4,5]
print("----------------")
print(multiply_num(*num)) # if we use * symbol before the argument the it unpack the item 
# OUTPUT
# (2,3,4,5)
# 120