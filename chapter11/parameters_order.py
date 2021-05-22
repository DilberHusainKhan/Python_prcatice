# if we  have to define a function that take

# Normal parameter
# *args
# default Parameter
# **kwargs

# in a single function than we will have to follow a proper order
# fun(normal_parameter, *args, Default_Parameter, **kwargs)
# Example
# use this format according to demand.
def fun(name, *args, age = 23, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

fun(
    'Dilber',
    1,2,3,
    full_name= 'Humayun'
)
