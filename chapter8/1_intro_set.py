# set data type 
# unordered collection of unique items
s={1,2,3,2}
print(s)
# print(s[1]) #####shows error because of unordered


# to remove duplicate from list
l = [1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,8]
s2 = set(l)
print(f"list become set is {s2} and its type is {type(s2)}")
new_list = list(set(l))
print(f"new list {new_list}  and type is {type(new_list)}")


# to add items in the set ******** add(element) ********** 
s.add('Dilber')
s.add('Dilber')
print(s) 


#to remove items from the set ********** remove(element) *************discard(element)*******
# 1. remove method
s.remove('Dilber')
# s.remove(9)  keyerror : 9
print(s)

# 2 discard method
s.discard(9)  #it does not show error
print(s)
s.discard(1)
print(s)



