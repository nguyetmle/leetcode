/**
    Given an integer array nums of length n and an integer target, 
    find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
 */

// level: medium
// approach: sorting, 2 pointers

 class 3SumClosest {
    public int threeSumClosest(int[] nums, int target) {
        int ans = nums[0] + nums[1] + nums[2]; //initialize a sum of triplet
        Arrays.sort(nums);

        for (int i=0; i+2<nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            
            //choose nums[i] as the first num in the triplet
            //and search the remaining nums in [i+1,n-1] 
            int l = i+1;
            int r = nums.length-1;
            while (l<r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == target) 
                    return sum;
                if (Math.abs(sum-target) < Math.abs(ans-target))
                    ans = sum; //update ans if sum is closer to target than ans
                if (sum < target) 
                    l++;
                else    
                    r--;
            }
        }

        return ans;
    }
 }