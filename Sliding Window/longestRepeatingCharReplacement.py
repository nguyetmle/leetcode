"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Level: medium
Approach: use hashmap (counter) and sliding window to get the character with max frequency, 
then keep shrinking the window if it takes more than k operations to turn the substring to all same character
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSubstr = 0
        maxSameChar = 0
        counter = collections.Counter()

        l=0 #left pointer
        for r,char in enumerate(s): #expand the window with right pointer
            counter[char] += 1
            maxSameChar = max(maxSameChar, counter[char])

            #while it takes more than k operations to make all string containing the same letter
            while maxSameChar + k < r-l+1:
                #keep shrinking the window
                counter[s[l]] -= 1
                l += 1
            maxSubstr = max(maxSubstr, r-l+1)
        
        return maxSubstr