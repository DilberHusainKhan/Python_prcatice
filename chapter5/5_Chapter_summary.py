# list chapter summary
# list is a data structure that can hold any type of data

# create a list 
words = ['word1','word2']

# you can store anything inside list
mixed = [1,2,3,[4,5,6],'seven',8.0,None]

# list is ordered collection of items
# print(mixed[0])  #output 1
# print(mixed[3])  #output [4,5,6]

# add data to our list
# append method

# mixed.append('10') #[1,2,3,[4,5,6],'seven',8.0,None,10]
# mixed.append([10,20,30])  # [1,2,3,[4,5,6],'seven',8.0,None,[10,20,30]]

#mixed.extend([10,20,30])  #[1,2,3,[4,5,6],'seven',8.0,None,10,20,30]

#join two list
# l = l1+ l2 

# insert method :-  to insert an element in the list at give location 
# append and extend add element at last location of the list 

# mixed.insert(1,"insert") #[1,'insert',2,3,[4,5,6],'seven',8.0,None]
# print(mixed)

# remove data from list
# mixed.pop()  # remove last item
# mixed.pop[1]  #remove item at position 1

# remove
# mixed.remove('seven')
# print(mixed) #remove seven

# del statement or del operator
# del mixed[3]
# print(mixed)

# loop in list

# for i in mixed:
    # print(i) 
    