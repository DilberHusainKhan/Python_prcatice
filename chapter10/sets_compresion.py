# Set Compresion in python 
# Set do not have order.
# to print square of number
sq = {k**2 for k in range(1,11)}
print(sq)

# to print first letter of names in the list 
names = ['Dilber', 'Husain','Khan','Humayun','Anwar']
first = {name[0] for name in names}
print(first)