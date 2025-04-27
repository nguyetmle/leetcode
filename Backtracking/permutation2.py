"""
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Level: medium
Approach: hashmap for frequency counter of unique character + backtrack
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #to avoid duplicate permutation, consider each unique number (rather than each number) as a true candidate
        #build a hashmap with key-value pair = unique number-frequency -> use Counter
        ans = []

        def backtrack(path, counter):
            if len(path) == len(nums):
                return ans.append(list(path))
            
            for num in counter:
                if counter[num]>0:
                    path.append(num)
                    counter[num] -= 1

                    backtrack(path, counter)

                    path.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        return ans