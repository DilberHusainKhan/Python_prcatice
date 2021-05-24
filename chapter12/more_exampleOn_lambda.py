# Example 1
# To check even or not
def is_even(a):
    return a%2==0
print(is_even(7))
# Lambda expression
print('Lambda Expression output --->')
is_even2 = lambda a : a%2==0
print(is_even2(4))
print(is_even2(5))

# ----------------------------------#
# Example 2
# To print last character of the String 
def last_char(a):
    return a[-1]
print(last_char('Dilber'))
# Lambda Expression
last_char2 = lambda a : a[-1]
print(last_char2('humayun'))

# ----------------------------------#
# Lambda Expression with if else 
# Example 3
# To check weather the length of string is greater than 5 or not 
def check_len(s):
    if len(s)>5:
        return True
    else:
        return False
print(check_len('Dilber'))

# Lambda Expression
# with if else
check_length = lambda s : True if(len(s)>5) else False
print(check_length('dilber'))

# without if else
check_length2 = lambda s : len(s)>5
print(check_length2('huma'))