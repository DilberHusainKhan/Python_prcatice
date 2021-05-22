# **kwargs will only take dictionary.
# kwargs stands for keyword argument 

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} : {v}")
    
func(first_name = 'Dilber', last_name = 'Husain', study = 'B.Tech')

def new_fun(name, **kwargs):
    print(name)
    print(kwargs)

new_fun(['name','roll'],first_name = 'Humayun', last_name = 'Anwar', study = 'B.Tech')

# dictionary unpacking
d = {'name': 'Dilber Husain Khan','age':23}
print("-----------------------")
func(**d)