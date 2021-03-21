# Filter odd even number
# define function
# input
# list --->[1,2,3,4,5,6,7]
# output ---> [[1,3,5,7],[2,4,6]]

# def odd_even(l):
#     f_list = [[],[]]
#     for i in l:
#         if(i%2 != 0):
#             f_list[0].append(i)
#         else:
#             f_list[1].append(i)
    # return f_list

def odd_even(l):
    odd_list = []
    even_list = []
    for i in l:
        if(i%2 != 0):
            odd_list.append(i)
        else:
            even_list.append(i)
    output = [odd_list,even_list]
    return output
f1_list = [1,2,3,4,5,6,7]
print(odd_even(f1_list))