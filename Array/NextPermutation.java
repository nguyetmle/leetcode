/**
    Given an array of integers nums, find the next permutation of nums.
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    For example, the next permutation of arr = [1,2,3] is [1,3,2
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
 */

// level: medium
// approach: 2 pointers

class NextPermutation {
    public void nextPermutation(int[] nums) {
        int n = nums.length;

        //from back to front, find the first num < nums[i+1] 
        int i;
        for (i=n-2; i>=0; i--) {
            if (nums[i] < nums[i+1])
                break;
        }

        //from back to front, find the first num > nums[i], swap it with nums[i]
        if (i>=0) {
            for (int j=n-1; j>i; j--) {
                if (nums[j] > nums[i]){
                    swap(nums,i,j);
                    break;
                }
            }
        }

        //reverse from nums[i+1] till the end of array
        reverse(nums,i+1,n-1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start<end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}