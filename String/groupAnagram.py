"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Level: medium
Approach: sort + hashmap
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for word in strs:
            #sort each word in alphabetical ord
            #so all anagram has the same key in dict
            key = "".join(sorted(word))

            #append all anagrams to the same key            
            dic[key].append(word)
        
        return dic.values()