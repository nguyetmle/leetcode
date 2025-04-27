/**
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
*/

// level: medium
// approach: 1D dynamic programming
// dp[i] is the length of max subarray ENDING AT INDEX I   
// base case: dp[0] = nums[0]
// case 1: dp[i-1] < 0 => ignore the previous subarray, start the new subarray at i
// case 2: dp[i-1] > 0 => add i to the previous subarray => form a new subarray
// note: dp[i] is NOT the length of max subarray for [0...i]
// => to get the max subarray of the whole array, find the max value in dp[]
class MaximumSubarray {
    public int maxSubarray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0]; //base case

        for (int i=1; i<nums.length; i++) {
            dp[i] = Math.max(dp[i-1]+nums[i], nums[i]);
        }

        int ans = dp[0];
        for (int i=1; i<dp.length; i++) {
            ans = Math.max(ans, dp[i]);
        }

        return ans;
    }
}
