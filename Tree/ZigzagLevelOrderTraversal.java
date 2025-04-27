/**
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
    (i.e., from left to right, then right to left for the next level and alternate between).
 */

// level: medium
// approach: BFS -> use queue. 
// Modify from Level Order Traversal: add boolean zigzag and reverse after every level

class ZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        if (root==null)
            return res;

        queue.add(root); //enqueue
        boolean zigzag = true; // a boolean value to flip the traversal order

        while (!queue.isEmpty()) {
            List<Integer> level = new LinkedList<Integer>();
            int size = queue.size();

            for (int i=0; i<size; i++) {
                TreeNode v = queue.poll(); //dequeue

                if (zigzag)
                    level.add(v.value) //left to right -> add to end
                else
                    level.addFirst(v.value) //right to left -> add to front
                
                if (v.left != null)
                    queue.add(v.left);
                if (v.right != null)
                    queue.add(v.right);
            }

            res.add(level);
            zigzag = !zigzag; //reverse the zigzag boolean
            
        }

        return res;
    }
}