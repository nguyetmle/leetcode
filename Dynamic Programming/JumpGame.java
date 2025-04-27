/**
 * You are given an integer array nums. You are initially positioned at the array's first index, 
 * and each element in the array represents your maximum jump length at that position.
 * Return true if you can reach the last index, or false otherwise.
 * 
 * eg: 
 * Input: nums = [2,3,1,1,4]
 * Output: true
 * Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
 */

// level: medium
// approach: greedy algorithm -> continuously update the farthest reachable index 
// at any point, if current index is not reachable (current index < farthest reachable index) -> return false
// if farthest pos >= array.length, return true
 

public class JumpGame {
    public boolean canJump(int[] nums) {
        int farthestPos = 0;

        for (int i=0; i<nums.length; i++) {
            if (farthestPos < i) //if current index is not reachable
                return false;
            farthestPos = Math.max(farthestPos, nums[i]+i);
        }

        return true;
    }
}