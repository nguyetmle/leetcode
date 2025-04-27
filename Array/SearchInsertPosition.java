/**
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
 */

// level: easy
// approach: binary search

class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;

        while (l<=r) {
            int mid = (l+r)/2;

            if (nums[mid] == target)
                return mid; 
            else if (nums[mid] > target) 
                r = mid-1; 
            else
                l = mid+1;
        }

        return l;
    }
}