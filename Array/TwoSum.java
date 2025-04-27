/** 
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
*/ 

// level: easy 
// approach: hashmap

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        //initialize a hashmap to store the indices of 2 nums that add up to target
        Map<Integer, Integer> numToIndex = new HashMap<>();

        //loop through array
        for (int i=0; i<nums.length; i++) {
            //use hashmap to instantly check for difference value
            if (numToIndex.containsKey(target-nums[i]))
                //if found, return the pair of indices
                return new int[] {numToIndex.get(target-nums[i]), i};
            
            //else, add num and its index to the hashmap
            numToIndex.put(nums[i],i);
        }

        throw new IllegalArgumentException();
    }
}

//hashmap stores item in key-value pairs
//hashmap.put(key,value): add a pair of key-value to hashmap
//hashmap.get(key): to access a value in hashmap, use get() and refer to its key
//hashmap.containsKey(key): return true if hashmap contains the specified key