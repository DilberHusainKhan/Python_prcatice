# We create a function that take input as a list and 
# give the output as number of list presnt in the list
# Ex
# [1,2,3,[1,2],[3,4]] --> 2
# hint use type()

def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count

mixed =[1,2,3,[1,2],[3,4],[4,5]]
print(f"Number of  list are :- {sublist_count(mixed)}") 