# In *args with normal parameter we use an extra parameter 
# Ex
def multiply_num(num, *args): # we can't be swap the parameter like (*args, num) because *args store all the values in it. 
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_num(2,2,3))
# the Output is 6 because first parameter is stored in num and rest all stored in args
# We will have to enter a parameter for num because it shows an error "missing 1 required posigtional parameter"
# we can make args as empty "Shown is program Intro_to_Star_args"
print("---------------------------------------")
print(multiply_num(2))
