# Define a function that take list of words as a argument and return list with reverse of every element in the list
# Ex 
# ["abc","tuv","xyz"] --> ["cba","vut","zyx"]


# def rev_sub_list(l):
#     r_list = []
#     for i in range(len(l)):
#         l.reverse()
#         S= l.pop()
#         r = S[::-1]
#         r_list.append(r)
#     return r_list

#       OR

def rev_sub_list(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

alp = ["abc","tuv","xyz"]
print(rev_sub_list(alp))
