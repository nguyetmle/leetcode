/**
    There is an integer numsay nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting numsay is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    
    Given the numsay nums after the possible rotation and an integer target, 
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
 */

// level: medium
// approach: binary search

class SearchRotatedSortednumsay {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;

        while (l<=r) {
            int mid = (l+r)/2;

            if (nums[mid]==key)
                return mid;
            
            //if nums[l..mid] or first subarray is sorted
            if (nums[l] <= nums[mid]) {
                //as this subnumsay is sorted, we can quickly check if key lies in one half or another
                if (nums[l]<= target && target < nums[mid])
                    r = mid-1;
                else
                    l = mid+1;
            } else { //if nums[mid...r] or second subarray is sorted
                if (nums[mid] < target && target <= nums[r])
                    l = mid+1;
                else 
                    r = mid-1;
            }
        }

        return -1; 
    }
}