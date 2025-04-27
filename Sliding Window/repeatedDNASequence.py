"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Level: Medium
Approach: Hashset, Sliding window
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #initialize 2 hashset
        #one to check if a dna sequence is repeated in the string
        #one to ensure the result list is unique
        seen, res = set(), set()
        
        #keep a sliding window of size 10
        for l in range(len(s)-9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        
        return list(res)
            