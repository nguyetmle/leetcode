"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Level: medium
Approach: backtracking
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(start,path):
            #if finish 1 string, add to ans
            if len(path) == len(s):
                return ans.append("".join(path))
            
            #if char is a number, then add to path and keep exploring next char
            if not s[start].isalpha():
                path.append(s[start])
                backtrack(start+1,path)
                path.pop()

            #if char is a letter, then add the lowercase to path and keep exploring next char, then do the same with upperase
            else:
                path.append(s[start].lower())
                backtrack(start+1,path)
                path.pop()

                path.append(s[start].upper())
                backtrack(start+1,path)
                path.pop()

        
        backtrack(0,[])
        return ans