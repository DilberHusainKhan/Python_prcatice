def last_char(name):
    print(name[-1])   # give the last letter of name
    last = len(name)
    print(name[last-1])

name = input("Enter your name ")
last_char(name)
# even odd
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "Odd"

def odd_even_1(num):
    if num%2 == 0:
        return "even"
    return "Odd"
  

print(odd_even(23))
print(odd_even_1(2))

