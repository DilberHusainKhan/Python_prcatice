# String are immutable in python
# means it can't be update 
# we can't add new character in the String
#Example

s = "string"
y=s.title()
print(s)
# output is "string"
print(y)
#output is "String"

#List
l=['A','B','C']
print(l)
l.pop()
print(l)
l.append('X')
print(l)

#Output
#['A', 'B', 'C']
# ['A', 'B']
# ['A', 'B', 'X']
