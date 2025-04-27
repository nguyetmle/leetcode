/**
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * 
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 */

// level: medium
// hint: ans[i] = leftProduct[i] * rightProduct[i]

class ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        //calculate the product of all numbers to the left of nums[i]
        int left = 1;
        int[] leftProduct = new int[n];
        for (int i=0; i<n; i++) {
            if (i>0)
                left *= nums[i-1];
            leftProduct[i] = left;
        }

        //calculate the product of all numbers to the left of nums[i]
        int right = 1;
        int[] rightProduct = new int[n];
        for (int i=n-1; i>=0; i--) {
            if (i<n-1)
                right *= nums[i+1];
            rightProduct[i] = right;
        }

        //multiple the left side and right side
        int[] ans = new int[n];
        for (int i=0; i<n; i++) {
            ans[i] = leftProduct[i] * rightProduct[i];
        }

        return ans;
    }
}
