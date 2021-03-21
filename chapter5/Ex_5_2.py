# print reversed of list
# While loop and pop() and append()

# def rev_list(l):
#     revers = []
#     i= len(l)
#     while i > 0:
#         revers.append(l.pop())
#         i-=1
#     return revers

#For loop 
# def rev_list(l):
#     r_list = []
#     for i in range(len(l)):   # for i in range(1, len(l)+1):
#         r_list.append(l.pop())
#     return r_list

# reverse() method 
# def rev_list(l):
#     l.reverse()
#     return l  

# Using [: : -1]
def rev_list(l):
    return l[::-1]

num = list(range(1,6))
alp = ["A","B","C","D"]
print(rev_list(alp)) 
