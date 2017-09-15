# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
        
        
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    #create table
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    goal_x=goal[0]
    goal_y=goal[1]
    
    #0 step from goal to goal
    value[goal_x][goal_y]=0
    
    #initialize open list with goal
    #element of open list: [value, x,y]
    open=[[0,goal_x,goal_y]]
    
    
    while(True):
        #sort & reverse to get the lowest value first
        if(len(open)==0):
            break
        
        open.sort()
        open.reverse()
        node=open.pop()
        val=node[0]
        x=node[1]
        y=node[2]
        
        for i in range(len(delta)):
            x2=x+delta[i][0]
            y2=y+delta[i][1]
            if(x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0])): #x2,y2 within the range
                if(grid[x2][y2]==1):#if there is a wall,
                    # keep the value to be 99
                    pass
                
                elif (value[x2][y2]==99): #value not yet filled
                    value[x2][y2]=val+cost
                    open.append([val+cost,x2,y2])
                    
                
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
print(compute_value(grid,goal,cost))

