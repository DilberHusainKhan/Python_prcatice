# min and max  function
# min give minimum value 
# max give maximum value
number =[4,60,6,2]
print(min(number))
print(max(number))

# print the greatest difference 
# 60 - 2

def great_diff(l):
    return max(l)-min(l)

print(great_diff(number))