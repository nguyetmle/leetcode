"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Level: medium
Approach: use hashmap and sliding window
"""
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = Counter()
        ans = 0

        l=0
        for r, char in enumerate(s):
            #increment frequency counter for each character
            seen[char] += 1 

            #keep sliding the window if has repeating character
            while seen[char] > 1:
                seen[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)
        
        return ans
