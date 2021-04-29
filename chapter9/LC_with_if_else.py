number = list(range(1,11))
print(number)
# to print even number from a given list.
even_num = [i for i in number if i%2==0]
print(even_num)

# to print even number from range 
even_num2 = [i for i in range(1,11) if i%2 == 0]
print(even_num2)

# to print odd number from a givven list
odd_num = [i for i in number if i%2 != 0]
print(odd_num)

# to print odd number form range 
odd_num2 = [i for i in number if i%2 == 1] 
print(odd_num2)

