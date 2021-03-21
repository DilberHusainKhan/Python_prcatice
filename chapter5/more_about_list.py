# Generate lists with range functions
# something more about pop methord
# index method
# pass list to function

# Generate lists with range functions
number= list(range(1,11))
print(number)

# pop()
# pop() can return value we can retrive that value
num = number.pop()
print(num)
print(number)

# index method
number.append(5)
print(number)
t=number.index(5)
# number.index(search_value, start_pos, end_pos)
print(t)

# pass list to function
num_list = list(range(1,11))
print(num_list)

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(num_list))