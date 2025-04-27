/**
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
 */

//level: easy
//approach: compare each character of string 0 to that of every other string starting from string 1
//NOTE: learn trie

class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0)
            return "";

        //loop through each character of string 0
        for (int i=0; i<strs[0].length(); i++) {
            //loop through each string from string 1 
            for (int j=1; j<strs.length; j++) {
                //compare with string 0
                //need to include the first condition to avoid index out of bound error
                if ((i==strs[j].length()) || strs[j].charAt(i) != strs[0].charAt(i))
                    return strs[0].substring(0,i);
            }
        }

        return strs[0];
    }
}