# Lambda expression also called anonymous function
# It can take any number of arguments, but can only have one expression
# Syntax:-  lambda arguments : expression
# Ex

# to add two number
add = lambda a,b : a+b
print(add(3,2))

# TO multiply two number
mul = lambda a,b: a*b
print(mul(2,3))

# To Print square of number
sqr = lambda a : a**2
print(sqr(4))

# to check anonymous 
print(add)
# Output:-  <function <lambda> at 0x00000273AAE47310> 