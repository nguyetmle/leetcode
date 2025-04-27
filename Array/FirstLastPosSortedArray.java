/**
    Given an array of integers nums sorted in non-decreasing order, 
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
 */

// level: medium
// approach: binary search

class FirstLastPosSortedArray {
    public int[] searchRange(int[] nums, int target) {
        int l = firstGreaterEqual(nums,target);
        if (l == nums.length || nums[l] != target) 
            return new int[] {-1,-1};
        int r = firstGreaterEqual(nums,target+1) - 1;
        return new int[] {l,r};
    }

    // find the first index l such that nums[l] >= target
    // return nums.length if can't find
    private int firstGreaterEqual(int[] nums, int target) {
        int l = 0;
        int r = nums.length;

        while (l<r) { //notice we do not compare element at mid with our target
            int mid = (l+r)/2;
            if (nums[mid] >= target)
                r = mid;
            else   
                l = mid+1;
        }

        //at this point (l==r) our search space has shrinked to 1 element
        //if current element is the target, return its index
        //else, element is not found
        return l;
    }
}