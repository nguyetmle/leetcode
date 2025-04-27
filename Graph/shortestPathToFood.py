"""
You are starving and you want to eat food as quickly as possible. 
You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

Level: medium
Approach: BFS

find location of *, start queue = coord of *
while queue:
    for each level:
        curr_cell = q.popleft()
        
        if curr_cell = #:
            return count
            
        if valid move: not out of bound + not X + not visited:
            change curr_cell to visited
            for direction in directions:
                add all neighbors to queue   
    count += 1 

return -1
"""
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        def isValid(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] != "X"

        def getStartPos():
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == "*":
                        return (r,c)
          
        i,j = getStartPos()
        queue = deque()
        queue.append((i,j)) 
        seen = {(i,j)} #a dictionary for visited node

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        step = 0

        while queue:
            queueLength = len(queue)
            for i in range(queueLength): #visit each element in current level
                i,j = queue.popleft()  

                if grid[i][j] == "#": #found food
                    return step
                
                for dx,dy in dirs: #add valid neighbors of each element to the queue, will visit them in the next level
                    newI, newJ = i+dx, j+dy
                    if isValid(newI,newJ) and (newI,newJ) not in seen:
                        queue.append(newI,newJ)
                        seen.add((newI,newJ))                       
            step += 1 #up one level so increment step
        
        return -1


        




