'''
we take the input as follows [[1, 0], [0, 1]] python doesn't understand it as list it just string 
all i want to do is to remove braket from the first and last of the input and remove spaces then split the string into array
so the input stored in In become ['[1','0]','[0','1]']
'''

In = input()[1:-1].replace(" ", "").split(",")

ls = []
ls_in = []
for i in In:                                    #check every elemnt of the list
    if i == '[]':                                # if it was empty 
        ls_in = [[]]                              #store in ls_in empty list 
    elif i[0] == '[' and i[-1] == ']':             #if it start with [ and end with ] then it mean it has one element in the array 
        ls.append(int(i[1:-1]))                    #store this element in list
        ls_in.append(ls)                            #then store this list into the list will be printed
    elif i[0] == '[' :                              #if it starts with [ 
        ls.append(int(i[1:]))                       #then remove the braket and store it in list
    elif i[-1] == ']':                               #if it ends with list it's mean our first list ends 
        ls.append(int(i[:-1]))                       #so we remove the braket to store first elemnt 
        ls_in.append(ls)                             #and append the finished list to list will be printed
        ls =[]                                        #and clear ls element
    else:
        ls.append(int(i))                            # it doesn't contain any brakets append direct
if len(ls_in) >1:                                     #if not empty or containing one element
    print([[row[i] for row in ls_in] for i in range(len(ls_in[0]))])#then transpose
else:
    print(ls_in) #else print the list 