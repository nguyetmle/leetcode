/**
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
 */

// level: medium

import java.util.*;

class FirstOccurrenceInString {
    public int strStr(String haystack, String needle) {
        int m = haystack.length();
        int n = needle.length();

        for (int i=0; i<m-n+1; i++) {
            if (haystack.substring(i,i+n).equals(needle))
                return i;
        }

        return -1;
    }
}

//time: O((m-n)*n)
