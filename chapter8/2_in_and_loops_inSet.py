# in and loops in set 
# in keyword in set and for loop 
s={'a','b','c'}
# in keyword to check if item is present or not in set
if 'a' in s:
    print('Present')
else:
    print("not Present")

# for loop in set 
for item in s:
    print(item)

# List l convert to set s
l=[1,1,2,2,3,4,4,5]
s= set(l)
print(s)

# set maths function

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

# UNION OF TWO SET
union_set = set_1 | set_2
print(union_set)

# INTERSECTION OF SET
intersection_set = set_1 & set_2
print(intersection_set)