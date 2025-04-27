/**
 * Given an integer array nums and an integer k, return the k most frequent elements. 
 * You may return the answer in any order.
 * 
 * eg: 
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 */

// level: medium
// approach: hashmap + bucket sort -> build an array of lists to be buckets, store numbers into different buckets whose index is the frequency


class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        //frequency map
        Map<Integer,Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n,0)+1);
        }

        //bucket sort on frequency
        List<Integer>[] bucket = new List[nums.length+1] // index starts from 1 because the frequency starts from 1
        for (int n : map.keySet()) {
            int freq = map.get(n); //get frequency of each number
            if (bucket[freq] == null) 
                bucket[freq] = new LinkedList<>();
            bucket[freq].add(n); //add number to the bucket whose index is the frequency
        }

        //iterate from the end of the bucket array (highest->lowest frequency)
        List<Integer> res = new ArrayList<>();
        for (int i = bucket.length-1; i>0 && k>0; i--) {
            if (bucket[i] != null) {
                res.addAll(bucket[i]);
                k -= bucket[i].size();
            }
        }

        //convert list<integer> to int[]
        int[] ans = new int[res.size()];
        for (int i=0; i<res.size(); i++)
            ans[i] = res.get(i);

        return ans;
    }
}