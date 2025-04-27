/**
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
 */

// level: medium
// approach: sort the array and use 2 pointers 

import java.util.*;

class 3Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3)
            return new ArrayList<>();
        
        List<List<Integer>> ans = new ArrayList<>();
        
        //sort the array
        Arrays.sort(nums);

        for (int i=0; i+2<nums.length; i++) {
            if (i>0 && nums[i] == nums[i-1]) //skip duplicate numbers
                continue;
            
            //choose nums[i] as the first num in the triplet
            //and search the remaining nums in [i+1,n-1]

            int l = i+1;
            int r = nums.length-1;
            while (l<r) {
                int sum = nums[i] + nums[l] + nums[r]; //calculate sum
                
                if (sum==0) {                  //if sum == 0
                    ans.add(Arrays.asList(nums[i],nums[l],nums[r])); //add the triplet to the ans
                    l++; //only need to update 1 pointer because other else-if conditions will update the other pointer accordingly
                    while (l<r && nums[l] == nums[l-1]) 
                        l++; //to skip duplicate
                } else if (sum<0) {  
                    l++;  //increment left pointer to increase the sum bc array is sorted 
                } else {
                    r--;  //decrement right pointer to decrease the sum bc array is sorted
                }
            }
        }

        return ans;
    }
}