/**
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 */

// level: medium
// approach: backtrack, recursion

import java.util.*;

class GenerateParentheses {
    public List<String> generateParentheses(int n) {
        List<String> ans = new ArrayList<>();

        //initially pass the counts of open and close as 0, and string s as an empty string
        backtrack(n,0,0,"",ans);
        return ans;
    }

    private void backtrack(int n, int open, int close, String s, ArrayList<String> ans) {
        //open: count of the number of open parentheses used in s
        //close: count of the number of close parentheses used in s
        //s: currently generated string
        //ans: list of strings to store all valid parentheses

        //if count of both open and close parentheses reaches n, 
        //it means we have generated a valid parentheses
        if (open == n && close == n) {
            //add currently generated string s to the final ans and return
            ans.add(s);
            return;
        }

        //at any index i in the generation of string s
        //we can put an open parentheses only if its count < n
        if (open < n) 
            backtrack(n,open+1,close,s+"(",ans);

        //at any index i in the generation of string s
        //we can put a close parentheses only if its count < the count of open parentheses
        if (close < open)
            backtrack(n,open,close+1,s+")",ans);
    }
}