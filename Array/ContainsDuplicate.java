/**
 * Given an integer array nums, return true if any value appears at least twice in the array, 
 * and return false if every element is distinct.
 */

// level: easy
// approach: hashmap -> count frequency

class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            if (map.containsKey(nums[i])) { //if number already appears, return true
                return true;
            }

            map.put(nums[i],1); //put the number appeared into hashmap
        }

        return false;
    }
}