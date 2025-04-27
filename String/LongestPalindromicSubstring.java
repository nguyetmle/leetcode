/**
    Given a string s, return the longest palindromic substring in s.
*/

// level: medium
// approach: 2 pointers - loop through each character (treat it as the middle char for each substring) 
// and check the if s[left] == s[right]. 
// **CHECK 2 CASES: length of substring can be odd or even 

class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        int resLen = 0;
        int resLeft = 0;
        int resRight = 0;

        for (int i=0; i<s.length(); i++) {
            //case 1: substring has odd length
            int l = i;
            int r = i;

            while (l >= 0 && r<s.length() && s.charAt(l)== s.charAt(r)) {
                //update the max substring if found new max
                if (l-r-1 > resLen) {
                    resLeft = l;
                    resRight = r;
                    resLength = resRight - resLeft + 1;
                }
                //move the left and right pointer outwards
                l--;
                r++;
            }

            //case 2: substring has even length
            l=i;
            r=i+1;
            
            while (l >= 0 && r<s.length() && s.charAt(l)== s.charAt(r)) {
                //update the max substring if found new max
                if (l-r-1 > resLen) {
                    resLeft = l;
                    resRight = r;
                    resLength = resRight - resLeft + 1;
                }
                //move the left and right pointer outwards
                l--;
                r++;
            }
        }

        return s.substring(resLeft,resRight+1);
    }
}