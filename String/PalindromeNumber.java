/**
    Given an integer x, return true if x is a palindrome, and false otherwise.
 */

// level: easy

class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x<0)
            return false;

        long reversed = 0;
        int y=x;
        
        while (y>0) {
            reversed = reversed*10 + y%10;
            y /= 10;
        }

        return reversed == x;
    }
}