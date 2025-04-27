/**
    Given the root of a binary tree, return the level order traversal of its nodes' values. 
    (i.e., from left to right, level by level).
 */

// level: medium
// approach: use queue

class LevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>(); //create a queue with linked list
        List<List<Integer>> res = new LinkedList<List<Intger>>(); //final result list

        //check if root is null
        if (root==null) 
            return res;

        //enqueue
        queue.add(root);

        //loop through each level in queue 
        while (!queue.isEmpty()) {
            List<Integer> level = new LinkedList<Integer>(); //list for each level
            int size = queue.size(); //update the queue size 
            //loop through each node in the same level
            for (int i=0;  i<size; i++) {
                TreeNode v = queue.poll(); //dequeue 
                level.add(v.val); 
                //enqueue left and right child
                if (v.left != null)
                    queue.add(v.left);
                if (v.right != null) 
                    queue.add(v.right);
            }

            res.add(level); //add each level to the final list
        }

        return res;
    }
}