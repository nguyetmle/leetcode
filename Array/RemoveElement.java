/**
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The relative order of the elements may be changed.
    Return k after placing the final result in the first k slots of nums.
 */

// level: easy
// approach: 2 pointers (similar to remove duplicates in sorted array)

class RemoveElement{
    public int removeElement(int[] nums, int target) {
        int l=0;

        for (int r=0; r<nums.length; r++) {
            if (nums[r] != target) {
                nums[l] = nums[r];
                l++;
            }
        }

        return l;
    }
}