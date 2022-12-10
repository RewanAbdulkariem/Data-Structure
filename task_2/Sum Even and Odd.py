# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
the user enter the input as [1, -1]
so we take the input from user remove first and last element to make input as follows 1,-1
then we can split it and store it in list named ls 
'''

input_ls = input()[1:-1].split(",")
sum_even = 0                    #intialize the sum of even numbers with 0
sum_odd = 0                     # do the same with sum of odd numbers
for i in input_ls:
    if i != '':                 # if the list is not empty
        if int(i)%2 == 0 :      #check if the element of list is even 
            sum_even = sum_even +int(i)       #then get the sum 
        else:                                 #if not even then it's odd 
            sum_odd = sum_odd + +int(i)       #get the sum 

output_ls = [sum_even,sum_odd]                #put the sum as a list and print it
print(output_ls)