/**
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?
 */

//level: easy
// hint: to reach point n, we can take one single step from point (n-1) or 2 steps from point (n-2)
//so total of ways to get to point n is: [n] = [n-1] + [n-2]

//approach 1: fibonacci-like 


// class ClimbingStairs {
//     public int climbStairs(int n) {
//         //base cases
//         if (n<=0) return 0;
//         if (n==1) return 1; //there is only 1 way to climb
//         if (n==2) return 2; //there are 2 ways to climb

//         //starting from n=3
//         int one_step_before = 2; //number of ways until point (n-1)
//         int two_step_before = 1; //number of ways until point (n-2)
//         int sum = 0;

//         for (int i=2; i<n; i++) {
//             sum = one_step_before + two_step_before;
//             two_step_before = one_step_before;
//             one_step_before = sum;
//         } 

//         return sum;
//     }
// }


//approach 2: dynamic programming
class ClimbingStairs {
    public int climbStairs(int n) {
        if (n<=1)
            return 1;
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i=3; i<=n; i++) 
            dp[i] = dp[i-1] + dp[i-2];
        return dp[n];
    }
}