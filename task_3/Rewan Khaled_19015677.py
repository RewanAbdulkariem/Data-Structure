class players:
    def __init__(self,r,c,d,a,mat):            
        self.row = r
        self.colunm = c
        self.mat = mat 
        self.digit = d   
        self.area = a 

        self.elements_x = []                                             #list to store the postion of the elements in row which contain 3
        self.elements_y = []                                             #list to store the postion of the elements in column which contain 3

        self.output = []                                                 #list to store the output element 

    # this method to call search method for every element in the list and calculate the center method 
    # to get the the center 
        
    def find_players(self):                        
        for j in range(self.colunm):
            for i in range( self.row):
                #print("row= "+ str(i)+"," + "col=",str(j))

                self.search(i,j)
                #for x in range(self.row):
                #    print(self.mat[x])
                self.calculate_center(i,j)
        
        self.output = sorted(self.output)         #Sort the output in increasing order
        
    #-------------print the output with the format shown in hackerrank---------------
        print("[",end="")
        for i in self.output:
            print("("+str(i[0])+", "+str(i[1])+")",end="")
            if i != self.output[-1]:
                print(", ",end="")
        print("]")            
    #--------------------------------------------------------------------------------
    
    #---------------search method to search for digit entered-----------------------
    def search(self,y,x):
        if self.mat[y][x] == self.digit:
            self.mat[y][x] = '#'
            self.elements_x.append(x)
            self.elements_y.append(y)

            self.check_neighbour(y,x)
            
    #------method to check neighbour of the digit found by search method---------------
    #-----------------commented line was just for test------------------------
    def check_neighbour(self,i,j): 
        #print("mat[{}][{}] = ".format(i,j),end="")            
        #print(self.mat[i][j])
        '''
        first we check if i not equal 0 or lower 
        then we check the list item if it equal the digit entered
        then we replace the item by chosen charcter "#" to not to be checked again then call the function again 
        for this neighbour to check its neighbour
        and so on for other if conditions
        '''
        if not(i <= 0):
            if self.mat[i-1][j] == self.digit:             
                self.mat[i-1][j] = '#'
                self.elements_y.append(i-1)
                #print("element of y (i-1) " ,end="")
                #print(self.elements_y)
                self.check_neighbour(i-1,j)

        if not(i >= self.row-1):
            if self.mat[i+1][j] == self.digit: 
                self.mat[i+1][j] = '#'
                self.elements_y.append(i+1)
                #print("element of y (i+1) " ,end="")
                #print(self.elements_y)
                self.check_neighbour(i+1,j)
                

        if not(j <= 0) :
            if self.mat[i][j-1] == self.digit:
                self.mat[i][j-1] = '#'
                self.elements_x.append(j-1)
                #print("element of x (j-1) " ,end="")
                #print(self.elements_x)
                self.check_neighbour(i,j-1)
                

        if not(j >= self.colunm-1):
            if self.mat[i][j+1] == self.digit:
                self.mat[i][j+1] = '#'
                self.elements_x.append(j+1)
                #print("element of x (j+1)" ,end="")
                #print(self.elements_x)
                self.check_neighbour(i,j+1)
    
    '''
    calculate center at this method we calculate the postion of the first item checked 
    and then we calculate the position of the last item in row and column 
    and then get the center of the square surrounded by these items
    '''
    def calculate_center(self,y,x):       
        pos_y = 2*y+1
        pos_x = 2*x+1
        
        posx_updated = pos_x
        posy_updated = pos_y
        
        #print("posx = "+str(pos_x)+"posy = "+str(pos_y))


        num = (len(self.elements_x)+len(self.elements_y)-1)         # num store the number of elements checked that equal 3 ,(-1) because the two lists contain the position of first item 
        a = num * 4                                                 # area of the these squares
        if a >=self.area:                                           #check the threshold
            for i in set(self.elements_x):
                if i> x:
                    posx_updated +=2
                elif i< x:
                    posx_updated -=2
            for j in set(self.elements_y):
                if j> y:
                     posy_updated +=2
                elif j< y:
                    posy_updated -=2
                
            center_x = int((pos_x +posx_updated)/2)
            center_y = int((pos_y +posy_updated)/2)
            self.output.append([center_x,center_y])
        self.elements_x = []                        #reset the two lists again to check other items in the mat list given  
        self.elements_y = []

        

row,column = [int(_) for _ in input().split(",")]
matrix = []

for i in range(row):          
    row_string = input()
    row_list = [x for x in row_string]
    matrix.append(row_list)

Base = input()
area = int(input())

pos = players(row,column,Base,area,matrix)
pos.find_players()
