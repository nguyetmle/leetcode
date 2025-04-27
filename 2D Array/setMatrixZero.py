"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Follow up:
    - A straightforward solution using O(mn) space is probably a bad idea.
    - A simple improvement uses O(m + n) space, but still not the best solution.
    - Could you devise a constant space solution?

Level: medium
Approach: 
    - Space O(m+n): use 2 hashset to save the row and col that needs to be set 0s
    - Space O(1): use the 1st cell of row and col to be the flag for setting 0s 
    (Note: the 1st row and col has the same 1st cell (grid[0][0]) -> need a boolean flag to seperate)
"""
#approach 1: O(m+n) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        fillRow = set()
        fillCol = set()

        #store the row and col that needs to change
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    fillRow.add(r)
                    fillCol.add(c)
        
        #fill 0s to row and col
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in fillRow or c in fillCol:
                    matrix[r][c] = 0
                    
#approach 2: O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #since the first cell of row and column for the 1st row and 1st column is the same (matrix[0][0]) 
        #need an additional flag to seperate if we need to change 1st column or 1st row to all 0s
        #matrix[0][0] is the flag if need to fill 1st row with 0s
        fillFirstCol = False  #flag if need to fill 1st column with 0s

        #loop through each cell, if found a cell = 0, then mark the first cell of that row and column
        #then later change all that row and column to 0
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                fillFirstCol = True
            
            for c in range(1,len(matrix[0])):
                #store information in the 1st cell of row and col
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        #fill 0s for the matrix except the 1st row/col
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        print(matrix)

        #fill 0s to 1st row if needed
        if matrix[0][0] == 0:
            matrix[0] = [0] * len(matrix[0])

        #fill 0s to 1st col if needed
        if fillFirstCol: 
            for r in range(len(matrix)):
                matrix[r][0] = 0