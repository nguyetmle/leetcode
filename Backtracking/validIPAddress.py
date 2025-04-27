"""
A valid IP address consists of exactly four integers separated by single dots. 
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Level: medium
Approach: use backtracking to find all the possible combinations of 4 numbers in the valid IP address
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(start,path):
            #if already finished forming all 4 numbers and reached end of string, add the address to res
            if len(path) == 4 and start == len(s):
                return ans.append(path[0] + "." + path[1] + "." + path[2] + "." + path[3])
            #if either have 4 numbers or reached end of string (but not both), then the address is not valid, backtrack to find other combinations
            if len(path) == 4 or start == len(s):
                return
            
            for length in range(1,4): #length of a integer in a valid address is from 1 to 3
                #a valid number in the IP address must not be: out of bound, have leading zero and > 255
                if start + length > len(s): #if out of bound
                    return
                if length>1 and s[start] == "0": #if has leading zero
                    return 
                #if > 255
                number = s[start : start+length]
                if int(number) > 255:
                    return
                
                #if it doesn't fall into those 3 cases, then it's a valid number
                path.append(number)
                backtrack(start+length, path)
                path.pop()
        
        backtrack(0,[])
        return ans
                
            

