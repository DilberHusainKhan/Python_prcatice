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

# to clear the set we use .clear() method
s.clear()
print(s)
s.add(2)
s.add(3)
s.add(7)
# to make copy we use copy method
print(s)
s4 = s.copy()
print(f"old set is {s} and new set is {s4}")

# we can also store float, int , bool etc. in set
set_1 = {1,1.0,1.1} # note 1 = 1.0
print(set_1)