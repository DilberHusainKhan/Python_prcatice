# Word Counter
# dilber
# {'d': 1, 'i': 1 ...}
s = (input("Enter String ").lower()).strip()
def Word_counter(s):
    counter ={}
    for i in s:
        counter[i] = s.count(i)
    return counter
print(Word_counter(s))
