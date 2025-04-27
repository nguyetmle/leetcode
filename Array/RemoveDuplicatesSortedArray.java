/**
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same.
    Return k after placing the final result in the first k slots of nums.
 */

// level: easy
// approach: 2 pointers 
// 1 pointer to scan through the array, 
// 1 pointer to keep track of the position of the next unique value

class RemoveDuplicatesSortedArray {
    public int removeDuplicates(int[] nums) {
        int l = 1;

        for (int r=1; r<nums.length; r++) {
            if (nums[r] != nums[r-1]) {
                nums[l] = nums[r];
                l++;
            }
        }

        return l;
    }
}

