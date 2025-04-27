/**
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.
    
    You are given an API bool isBadVersion(version) which returns whether version is bad. 
    Implement a function to find the first bad version. 
    You should minimize the number of calls to the API.
*/

//level: easy
//approach: binary search

class 1stBadVersion {
    public int firstBadVersion(int n) {
        int lo = 1;
        int hi = n;
        int ans = -1;

        while (lo<=hi) {
            //select a mid element
            int mid = lo + (hi-lo)/2;
            //if isBadVersion(mid)==true => all right part of mid is true
            //save mid and move the search space to left
            if (isBadVersion(mid)) {
                ans = mid;
                hi = mid-1;
            }
            //if isBadVersion(mid)==false => all left part of mid is false
            //move the search space to right
            else 
                lo = mid+1;
        }
        //get out of while loop when space converges to 1 element
        return ans;
    }
}