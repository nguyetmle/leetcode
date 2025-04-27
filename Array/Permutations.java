/**
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.
 */

//level: medium
//approach: depth first search, backtracking

class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        dfs(nums, new boolean[nums.length], new ArrayList<>(), ans);
        return ans;
    }

    private void dfs(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> ans) {
        //base case
        //when have enough numbers to form a permutation (path)
        //add to ans
        if (path.size() == nums.length) {
            ans.add(new ArrayList<> path);
            return;
        }

        //traverse the array
        for (int i=0; i<nums.length; i++) {
            if (used[i])
                continue;
            //visit each number and mark as visited
            used[i] = true;
            path.add(nums[i]);
            //call the dfs on the new path until find a permutation
            dfs(nums,used,path,ans);
            //at this point, a permutation is formed
            //backtrack to the path before 
            //remove the last number in that path to form a new path
            path.remove(path.size()-1);
            used[i]=false;

        }
    }

}
