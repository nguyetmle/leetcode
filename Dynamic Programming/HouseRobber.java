/**
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
    and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
*/

//level: medium
//approach: dynamic programming

//f(n) = max money of robbing house [0,1,2,...,n]
//An = amount of money at the n-th index house.

// At each house we have the choice of robbing it or leaving it.
// case 1 – if we pick last house:
// then, we cant pick (n-1)th house, hence f(n)= An + f(n-2)
// case 2 – if we leave last house:
// then, we will stick with the max profit till (n-1)th house, hence f(n)= f(n-1)

//=> f(n) = max(An + f(n-2), f(n-1))
//if use recursion => O(2^n)
//=> use dynamic programming approach and store the intermediate results in an array.
//after calculating we will return the value stored at nth(last) index in array.

class HouseRobber {
    public int rob(int[] nums) {
        int prev1 = 0;  //f(n-1)
        int prev2 = 0;  //f(n-2)

        for (int num : nums) {
            int dp = Math.max(prev1, num+prev2);
            prev2 = prev1;
            prev1 = dp;
        }

        return prev1;
    }
}

