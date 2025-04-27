"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Level: easy
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #2 people climbing from left and right
        #if there is only 1 mountain
        #they will meet at the peak
        i, j = 0, len(arr)-1
        while i+1<len(arr) and arr[i] < arr[i+1]:
            i += 1
        while j>0 and arr[j-1] > arr[j]:
            j -= 1
        return i>0 and j<len(arr)-1 and i==j  