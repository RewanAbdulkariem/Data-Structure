'''
the user enter the input as [1, -1]
so we take the input from user remove first and last element to make input as follows 1,-1
then we can split it and store it in list named ls 
'''

ls = input()[1:-1].split(",")  
new_ls=[]                               #output list to be printed
for i in ls:                            
    if i != '':                         #if list is not an empty list 
        new_ls.insert(0,int(i))         #then take every element of the list and put it in the first of the list
        

print(new_ls)