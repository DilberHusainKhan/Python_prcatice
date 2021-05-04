# List comprehension in nested list
# ex we generate [[1,2,3],[1,2,3],[1,2,3]]

nested_list = [[i for i in range(1,4)] for j in range(3)]
print(nested_list)

nested_lst = []
for j in range(3):
    nested_lst.append([1,2,3])
print(nested_lst)

# for a given list if we found any odd number the we should make it negative 
# else if a number if number is even then multiply by 4 
# 
old_list = [1,2,3,4,5,6]
new_list = [i**2 if(i%2 == 0) else -i for i in old_list]
print(new_list)
