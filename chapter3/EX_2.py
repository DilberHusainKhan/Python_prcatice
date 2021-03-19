# Sum of N natural number 
total = 0
i=1
N = int(input("Enter any number"))
while i<N:
    total+= i
    i+=1
print(f"The total sum is {total}")

#  sum of digit of a number
number_1 = input('Enter any number "sum of digit of a number"')
total_1=0
j=0
while j <= len(number_1): 
    total_1 += int(number_1[j])
    j += 1
print(total_1)