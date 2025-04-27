"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. 
In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

eg: 
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Level: Medium
Approach: Sort then Sliding window
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  #so we know it costs the least operations to increase nums[i-1] and convert it into nums[i]

        #create a sliding window
        l,r = 0,0
        res,total = 0,0

        while r < len(nums):
            total += nums[r]

            #calculate the cost of converting all numbers in the current window into nums[r]
            #while it's bigger than total + k (which means we don't have enough k operations to do the conversion), keep shrinking the window
            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1
            
            #else, calculate the window length and keep expanding the window
            res = max(res, r-l+1)
            r += 1
        
        return res
                