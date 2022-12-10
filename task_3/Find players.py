class players:
    def __init__(self,r,c,mat):
        self.row = r
        self.colunm = c
        self.matrix = mat
        self.countx = 1
        self.county= 1
        self.visited = [[False for j in range(self.colunm)]for i in range(self.row)]
    
    def find_players(self):
        print("[",end="")
        for i in range(self.row):
            for j in range( self.colunm):
                print("i= "+ str(i)+"," + "j=",str(j))
                print("elment is"+str(self.matrix[i][j]))
                self.check(i,j)
                if self.countx > 1 or self.county > 1:
                    center_pos = self.calculate_postion(self.countx,self.county,i,j)
                    print("(" + str(center_pos[0]),", ",str(center_pos[1]),")",",", end="")
                self.countx = 1
                self.county = 1

            
        print("]")


    def check(self,i,j):
        print ("check is ",end="")
        print(self.matrix[i][j].isdigit())
        if self.matrix[i][j].isdigit() and self.visited [i][j] ==False:
            digit = self.matrix[i][j]
            print("digit is"+ str (digit))
            self.visited[i][j] =True
            self.check_neighbour(i,j,digit)
    
    def check_neighbour(self,i,j,digit):
        print ("i = ",str(i),"j= ",str(j))
        if not(i <= 0):
            if self.matrix[i-1][j] == digit: 
                self.check(i-1,j)
                self.countx = self.countx +1
                print("countx = ",str(self.countx))
        if not(i >= self.row):
            if self.matrix[i+1][j] == digit: 
                self.check(i+1,j)
                self.countx = self.countx +1
                print("countx = ",str(self.countx))

        if not(j <= 0) :
            if not(j <= 0 ) and self.matrix[i][j-1] == digit:
                self.check(i,j-1)
                self.county = self.county +1
                print("county = ",str(self.county))

        if not(j >= self.colunm):
            if self.matrix[i][j+1] == digit:
                self.check(i,j+1)
                self.county = self.county +1
                print("county = ",str(self.county))


    def calculate_postion(self,x_elements,y_elements,i,j):
        pos_x = 2*i+1
        pos_y = 2*j+1
        posx_updated = pos_x + 2 * x_elements -2
        posy_updated = pos_y + 2 * y_elements -2
        center_x = int((pos_x +posx_updated)/2)
        center_y = int((pos_y +posy_updated)/2)
        center = [center_x,center_y]
        return center


        

        



row,column = [int(_) for _ in input().split(",")]
matrix = []

for i in range(row):          
    row_string = input()
    row_list = [x for x in row_string]
    matrix.append(row_list)

pos = players(row,column,matrix)
pos.find_players()

