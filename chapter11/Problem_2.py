# print the first leter of all element in the list as captial if user will enter only name
# print(func(name))
# if user will enter name as well as reverse_str = true then it will return 
# reverse of string and the captialised first leter.
from typing import no_type_check_decorator



def func(l, **kwargs):
    if(kwargs.get('reverse_str')):
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

print(func(['dilber','khan']))
print(func(['dilber','khan'], reverse_str = True))