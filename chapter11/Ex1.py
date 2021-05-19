# define a function 
# input 
# num, iterable(tuple ,list) contain number as args
# Example
# Input num= [1,2,3]
# to_power(3,*nums)
# Output 
# list ---> [1,8,27]
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "hey you didn't enter any argument"  
nums = [1,2,3]
print(to_power(3,*nums))
