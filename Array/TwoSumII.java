/**
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, 
    added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.
 */

//level: medium
//approach: SORTED ARRAY-> use 2 pointers from start and end of array, keep comparing sum to target to move either pointer as necessary

class TwoSumII {
    public int twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length-1;
        int[] res = new int[2];

        while (start<end) {
            int sum = numbers[start] + numbers[end];

            if (sum < target)
                //move the start pointer to make sum bigger
                start++;
            else if (sum > target)
                //move the end pointer to make sum smaller
                end--;
            else {
                res[0] = start+1;
                res[1] = end+1;
                return res;
            }
        }

        return res;
    }
}