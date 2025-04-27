/**
    Given two strings text1 and text2, return the length of their longest common subsequence. 
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters 
    (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

    A common subsequence of two strings is a subsequence that is common to both strings.
 */

// level: medium
// approach: 2D dynamic programming
// dp[i][j] = LCS's length of text1[0...i] and text2[0...j]
// base case: dp[0][i] = 0 and dp[j][0] = 0 for i=0,1,..,text1.length, j=0,1,..,text2.length
// case 1: text1[i] = text2[j] => add 1 to the LCS's length of text1[0...(i-1)] and text2[0...(j-1)]
// case 2: text1[i] != text2[j] => check LCS for text1[i]-text2[j-1] and text1[i-1]-text2[j]

class LongestCommonSubsequence {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        int[][] dp = new int[m+1][n+1];
        //in java, int[][] auto fill 0 when initializing

        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                if (text1.charAt(i) == text2.charAt(j))
                    dp[i][j] = 1 + dp[i-1][j-1];
                else 
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }

        return dp[m][n];
    }
}