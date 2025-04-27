"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Level:medium
Approach: backtracking
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curStr, leftCount, rightCount):
            if len(curStr) == 2*n: #finish a valid parenthesis string
                res.append("".join(curStr))
                return 
            if leftCount < n: 
                #then a left parenthesis can still be added
                curStr.append("(")
                backtrack(curStr,leftCount+1,rightCount)
                curStr.pop()
            if rightCount < leftCount:
                #then a right parenthesis can still be added
                curStr.append(")")
                backtrack(curStr,leftCount,rightCount+1)
                curStr.pop()
        
        backtrack([],0,0)
        return res