"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Level: medium
Approach: sliding window
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        if len(s) < len(p):
            return res
        
        #create 2 arrays to store character frequency
        sCount = [0] * 26
        pCount = [0] * 26

        #create window of size len(p)
        #count char frequency in p and in first window of s
        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1
        
        #sliding window on s
        for i in range(len(s)-len(p)+1):
            if sCount == pCount:
                res.append(i)
            #add one more char to the right side of window
            if i + len(p) < len(s):
                sCount[ord(s[i + len(p)]) - ord('a')] += 1

            #remove starting char in window
            sCount[ord(s[i]) - ord('a')] -= 1

        
        return res