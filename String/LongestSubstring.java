/**
    Given a string s, find the length of the longest substring without repeating characters.
*/

// level: medium
// approach: sliding window, if we see same character within the current window, shift start position of window
import java.util.*;

class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        int[] count = new int[128]; //initialize empty array to count frequency of character

        //loop through string
        for (int l=0, r=0; r<s.length(); r++) {
            //increment the frequency counter of a character
            count[s.charAt(r)]++;
            //while a character appears > 1 
            while (count[s.charAt(r)] > 1) {
                //shift the start position of the window to after the first occurence of the repeated char
                //and decrement frequency counter of all character before that
                count[s.charAt(l)]--;
                l++;
            }
            //calculate length of window
            ans = Math.max(ans, r-l+1);
        }

        return ans;
    }
}