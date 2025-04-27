"""
You may recall that an array arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain. 
Return 0 if there is no mountain subarray.

Level: Medium
Approach: 2 pointers
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #left and right pointers starting at the same point, keep the left pointer unmoved while moving right pointers till the end of the mountain, calculate length
        #update left and right pointer again and repeat to find all mountains 

        l,r = 0,0
        maxLength = 0
        n = len(arr)
        while l < n-2:
            #skipping descending and equal array
            while l<n-1 and arr[l] >= arr[l+1]:
                l += 1
            
            #moving right pointer up the moutain
            r=l+1
            while r<n-1 and arr[r] < arr[r+1]:
                r += 1
            
            #moving right pointer down the moutain and calculate mountain length
            while r<n-1 and arr[r] > arr[r+1]:
                r += 1
                maxLength = max(maxLength, r-l+1)
            
            #move to new mountain
            l=r
        
        return maxLength

