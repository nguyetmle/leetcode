'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s.

eg 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

eg 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

eg 3: 
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Level: Easy
Approach: Hashmap
'''



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        charToWord = {}
        #for every char in pattern list, check if there is a mapping to a word in word list
        for i in range(len(pattern)):
            #if char is mapped to a word, check if there is any unmatched mapping
            if pattern[i] in charToWord.keys():
                if charToWord[pattern[i]] != words[i]:
                    return False

            #if char is not in map, add char to map
            else:
                #need to check the case that, there is no key in map but value already exists
                #for example, pattern = "abab" && s = "dog dog dog dog"
                if words[i] in charToWord.values():
                    return False
                else:
                    charToWord[pattern[i]] = words[i]
        

        return True