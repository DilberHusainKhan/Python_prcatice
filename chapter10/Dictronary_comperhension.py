# Like List comprehension dictionary Comprehension is same
# EX- to print square of number form 1 to 10 using dictionary comprehension
square ={num:num**2 for num in range(1,11)}
print(square)

# to print square like that num is num
square1 = {f"Square of {num} is ": num**2 for num in range(1,11)}
print(square1)
for k,v in square1.items():
    print(f"{k} :{v}")

# To Print count of given String
string = "DilberDil"
word_count = {char : string.count(char) for char in string} 
print(word_count)