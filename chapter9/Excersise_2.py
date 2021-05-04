# num to String 

# input -------> [ True, False, [1,2,3], 1,1.0,2]
# output --------> ['1', '1.0', '2']
old_list = [True,False,[1,2,3,4], 1,1.1,2,3]
def num_to_String(old_list):
    new_list = [str(i) for i in old_list if type(i)==int or type(i) == float]
    print(new_list)
num_to_String(old_list)