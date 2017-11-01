# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def remove_gval(gVal_and_coords):
    return [gVal_and_coords[1], gVal_and_coords[2]]

def move(currentCell, movement):
    return [currentCell[0] + movement[0], currentCell[1] + movement[1]]
    
    
def isOpenCell(x, y, grid=grid):
    max_y = len(grid)
    max_x = len(grid[0])
    #print(str(max_y) + " x " + str(max_x) + " grid")
    isInsideGrid = (x >= 0 and x <=max_y - 1) and (y >= 0 and y <= max_x -1)
    
    #print(str(x) + "," + str(y))
    #print("isInsideGrid: " + str(isInsideGrid))
   
    if(isInsideGrid == False):
        #print("---")
        return False
    
    isBlocked = grid[x][y] == 1
    
    #print("isBlocked: " + str(isBlocked))    
    #print("---")
    
    return  isBlocked == False

def getNeighbors(cell, delta=delta):
    possibleNeighbors = [move(cell, m) for m in delta]
    validNeighbors = [x for x in possibleNeighbors if isOpenCell(x[0], x[1])] 
    return validNeighbors

def search(grid,init,goal,cost, g_val = 0):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open = [[g_val, init[0], init[1]]]
    #print("initial open list:")
    #print(open)
    #/prinprint("---")
    

    expanded = []
    while True:
        sortedItems = sorted(open, key=lambda open:open[0])
        if not sortedItems:
            return "fail"        
            
        itemToExpand = sortedItems.pop(0) 
        itemToExpandCoord = remove_gval(itemToExpand)
        #expanded.append(itemToExpandCoord) 


        if itemToExpandCoord == goal:
            return itemToExpand
        else:
            #print("take list item")
            #print(itemToExpand)
            expanded.append(itemToExpandCoord)
            neighbors = getNeighbors([itemToExpand[1], itemToExpand[2]])
            valid_neighbors = [n for n in neighbors if n not in expanded]
            for vn in valid_neighbors:
                expanded.append(vn)
            g_val += 1
            for n in valid_neighbors:
                sortedItems.append([itemToExpand[0]+1, n[0], n[1]])
            #print("new open list")
            #print(sortedItems)   
            open = sortedItems 

    
    #return path

result = search(grid, init, goal, cost)
print(result)


    
    
#print(getNeighbors([0,0]))    
'''  
assert isOpenCell(-1,0,grid) == False, 'NOT Inside'
assert isOpenCell(0,-1,grid) == False, 'NOT Inside'
assert isOpenCell(0,0,grid) == True, 'Inside'
assert isOpenCell(0,5,grid) == True, 'Inside'
assert isOpenCell(6,0,grid) == False, 'NOT Inside'
assert isOpenCell(0,4,grid) == True, 'Inside'

assert isOpenCell(0,2,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(1,2,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(2,4,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(3,2,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(3,3,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(3,4,grid) == False, 'NOT Open (BLOCKED)'
assert isOpenCell(4,4,grid) == False, 'NOT Open (BLOCKED)'

assert isOpenCell(4,5,grid) == True, 'Open'
'''