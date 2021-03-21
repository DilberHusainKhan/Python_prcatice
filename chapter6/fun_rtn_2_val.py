import time
# function returning two values
def func(int1, int2):
    start = time.time()
    add = int1+int2
    multiply = int1*int2
    end = time.time()
    print(end-start)
    return add, multiply

print(func(2,3))

# Output  
# function return tuple 

add, multiply = func(2,3)
print(add)
print(multiply)