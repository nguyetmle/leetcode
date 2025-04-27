/**
    Given an integer array nums where the elements are sorted in ascending order, 
    convert it to a height-balanced binary search tree.
 */

//level: easy
//approach: create a helper function to recursively make the median as the root of subtree/tree

class ConvertArrayToBST {
    public TreeNode sortedArrayToBST(int[] nums) {
        return createBST(nums, 0, nums.length-1);
    }

    private TreeNode createBST(int[] nums, int l, int r) {
        //base case
        if (l<r)
            return null;
        
        //to create a height-balanced BST from a sorted array,
        //make middle value as root
        int mid = l + (r-l)/2;
        TreeNode root = new TreeNode(nums[mid]);
        
        //recursively call the function to create left and right subtree
        root.left = createBST(nums, l, mid-1);
        root.right = createBST(nums, mid+1, r);
        return root;

    }
}