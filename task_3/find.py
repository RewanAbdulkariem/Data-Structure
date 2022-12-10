class players:
    def __init__(self,r,c,d,a,mat):
        self.row = r
        self.colunm = c
        self.mat = mat 
        self.digit = d   
        self.area = a 
        
        self.row_up = 0
        self.row_down = 0  
        self.colunm_r = 0
        self.colunm_l = 0 
        self.num = 1 
        self.elements_x = []
        self.elements_y = []


        
    def find_players(self):
        print("[",end="")
        for j in range(self.colunm):
            for i in range( self.row):
                print("row= "+ str(i)+"," + "col=",str(j))

                self.search(i,j)
                for x in range(self.row):
                    print(self.mat[x])
                self.calculate_center(i,j)
            
        print("]")
    
    
    def search(self,x,y):
        if self.mat[x][y] == self.digit:
            self.mat[x][y] = '#'
            self.check_neighbour(x,y)
            
    
    def check_neighbour(self,i,j):        
        if not(i <= 0):
            if self.mat[i-1][j] == self.digit: 
                self.row_up -= 1
                
                self.num += 1
                self.search(i-1,j)

        if not(i >= self.row-1):
            if self.mat[i+1][j] == self.digit: 
                self.row_down += 1
                self.num += 1

                self.search(i+1,j)
                

        if not(j <= 0) :
            if not(j <= 0 ) and self.mat[i][j-1] == self.digit:
                self.colunm_l -= 1
                self.num += 1

                self.search(i,j-1)
                

        if not(j >= self.colunm-1):
            if self.mat[i][j+1] == self.digit:
                self.colunm_r += 1
                self.num += 1

                self.search(i,j+1)
    
    def calculate_center(self,i,j):
        pos_y = 2*i+1
        pos_x = 2*j+1
        print("posx = "+str(pos_x)+"posy = "+str(pos_y))
        

        a = self.num*4
        if a >=self.area:
            if ( self.row_up + self.row_down) >=0:
                county = self.row_down +1
                posy_updated = pos_y + 2 * county -2
            else:
                county = self.row_up -1
                posy_updated = pos_y + 2 * county +2

            
            if ( self.colunm_r + self.colunm_l) >=0:
                countx = self.colunm_r +1
                posx_updated = pos_x + 2 * countx -2

            else:
                countx = self.colunm_l -1
                posx_updated = pos_x + 2 * countx +2
            
            print("posx_updated = "+str(posx_updated)+"posy = "+str(posy_updated))
            
            center_x = int((pos_x +posx_updated)/2)
            center_y = int((pos_y +posy_updated)/2)
            print("(" +str(center_x),", ",str(center_y),")")
        
        self.num =1
        self.row_up = 0
        self.row_down = 0  
        self.colunm_r = 0
        self.colunm_l = 0
        

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
