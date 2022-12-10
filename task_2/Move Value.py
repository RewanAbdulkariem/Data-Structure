'''
store the input taken from the user after removing the braket
then take the number wanted to cahnge its postion as an input 
check if list not empty  
and pop the elemnt from its postion and append it in last postion
'''
In = input()[1:-1] 
ls =[]
chosen_num = int(input())
for i in In:
    if i != '':
        ls = [int(x) for x in In.split(",")]
for i in ls:
     if chosen_num == i:
        ls.append(ls.pop(ls.index(i)))
print(ls)