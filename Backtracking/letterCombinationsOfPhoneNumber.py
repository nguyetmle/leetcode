"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Level: medium
Approach: backtrack
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return None
        
        #hashmap to map digits to letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []

        def backtrack(path,index):
            #add complete combination to res
            if len(path) == len(digits):
                res.append("".join(path))
                return
            #get all the letters that correspond with the current digit we are looking at
            possibleLetters = letters[digits[index]]

            #loop through each letter and add to combination
            for letter in possibleLetters:
                path.append(letter)
                backtrack(path,index+1) #explore all combinations for next digit
                path.pop()
        
        backtrack([],0)
        return res
