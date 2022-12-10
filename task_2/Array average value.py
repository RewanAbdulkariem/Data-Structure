'''
the user enter the input as [1, -1]
so we take the input from user remove first and last element to make input as follows 1,-1
then we can split it and store it in list named ls 
'''

ls = input()[1:-1].split(",")
sum= 0
for i in ls:
    if i != '':            #check if list is not empty 
        sum = sum +int(i)  #then get the sum of the list element
avarge = sum / len(ls)     #divide the sum over the lenght to get the avarge
print(avarge)