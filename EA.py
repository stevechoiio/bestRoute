

testSet = [
        [3, 2, 1],
        [3,-1, 2],
        [1,-1, 5]
    ]


class Search():
    def __init__(self,x,y,goalx,goaly,grid,closedSet):
        self.x = x
        self.y = y
        self.startingPoint = [x,y]
        self.goalPoint = [goalx,goaly]
        self.grid = grid
        # stores all the node that has been checked
        self.closedSet = []
        self.maxX = len(grid[0])
        self.maxY = len(grid)


    def search(self,x,y):
        if [x,y] in self.closedSet:
            return False
        else:   
            if self.grid[x][y] == -1:
                print('this is a wall')
                return False
            self.closedSet.append([x,y])
            print('the list of closedSEt is :',self.closedSet)
            
            if (x < self.maxX) & (y < self.maxY):
                print('checking: ',x,y)
                print('gas in this grid: ', self.grid[x][y])
                if self.grid[x][y] == -1:
                    print('this is a wall')
                    return False
                elif [x,y] == self.goalPoint:
                    print('done! have reached the end point')   
                else:
                    self.search(x+1,y)
                    self.search(x-1,y)
                    self.search(x,y+1)
                    self.search(x,y-1)
               

                
          
    def shout(self): 
        print(self.maxX)


    
        
test = Search(0,0,0,2,testSet,[])

test.search(0,0)


    # def search(self,x,y):
    #     if [x,y]  == self.startingPoint:
    #         print('done')
    #     elif self.grid[x][y] == -1:
    #         self.closedSet.append([x,y])
    #     else : 
    #         return false      
    
    # def setRange(self):
        
    #     for x in range(self.maxX):
    #         for y in range(self.maxY):
    #             self.search(self.x,self.y)

        


# class Search():
#     def __init__(self,x,y,goalx,goaly):
#         self.x = x
#         self.y = y
#         self.goalx = goalx
#         self.goaly = goaly
        
    
#     def printStatus(self):
#         print(self.x,self.y,self.goalx,self.goaly)
    
#     def calcStep(self):
#         count = 0
#         while [self.x,self.y] != [self.goalx,self.goaly]:
#             if self.x != self.goalx:
#                 self.x +=1
             
#             elif self.y != self.goaly:
#                 self.y +=1
#             count +=1
#             print('Count: ',count, 'X is: ',self.x, 'Y is: ',self.y)
#         print('reached the point, the job is done!')

#     def childNode(self):
#         openList  =[]       
#         openList.append()




# xyz = Search(1,3,22,44)
# xyz.calcStep()

