# Find the common element give two list 
# and 
# print the common elements as output list

def common_find(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

f_list = [1,2,3,4]
s_list = [4,2,7,1]
print(common_find(f_list,s_list))

# output
# [1,2,4]