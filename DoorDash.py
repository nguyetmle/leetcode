import collections
"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells

======
Approach 0: Brute Force
The first idea is to use brut-force
to generate all possible ways to fill the cells
with numbers from 1 to 9,
and then check them to keep the solution only.
That means 9^{81} operations to do,
where 9 is a number of available digits
and 81 is a number of cells to fill.
Hence we're forced to think further how to optimize.

Approach 1: Hash table, Backtracking
Let's imagine that one has already managed to
put several numbers on the board.
But the combination chosen is not the optimal one and there is no way
to place the further numbers. What to do? To backtrack.
That means to come back,
to change the previously placed number and try
to proceed again. If that would not work either, backtrack again.

How to enumerate sub-boxes: box_index = (row / 3) * 3 + column / 3

Time: Time complexity is constant here since the board size is fixed and there is no
N-parameter to measure.
Though let's discuss the number of operations needed : (9!)^9
Let's consider one row, i.e. not more than 999 cells to fill.
There are not more than 9 possibilities for the first number to put,
not more than 9×8 for the second one,
not more than 9×8×7 for the third one etc. In total that
results in not more than 9! possibilities for a just one row,
that means not more than (9!)^9 operations in total.

Space: The space complexity only considers auxiliary space.
The board is given and reused, so there is no auxiliary space added. 
From 1 to k (assuming there are k different numbers, this problem k = 9), 
when it cannot solve, before going to the next board[i][j], 
it backtracks all the way to the top and releases all the call stack memory usage. 
Therefore, the call stack can only go as far as k levels, which is constant, 
even when local variables are used the total space is still constant. 
Thus the space complexity is O(1), even when m and n becomes much bigger than k.

"""
class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:

    #check for valid sudoku
    def isValid(row: int, col: int, c: str) -> bool:
        for i in range(9):
            if board[i][col] == c or \
            board[row][i] == c or \
            board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solve(s: int) -> bool:
        if s == 81:
            return True

        i = s // 9
        j = s % 9

        if board[i][j] != '.':
            return solve(s + 1)
        
        #iterate through all the possible values of c from 1 to 9
        for c in string.digits[1:]:
            #if adding c to a cell makes a valid sudoku
            if isValid(i, j, c):
                board[i][j] = c 
                #and able to solve to the end, return true 
                if solve(s + 1):
                    return True
                board[i][j] = '.' #else, backtrack and go back to the previous state

        return False #no value fits current cell

    solve(0)
   

"""
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear 
in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

=====
Approach 0: Brute Force
Look at all possible paths, calculate their path sums, and then find the maximum path sum.
=> O(n^2)

Approach 1: Post Order DFS

Consider a scenario where the path with the highest sum passes through the tree's root.

There could be four possibilities.

- The path starts at the root and goes down through the root's left child. 
We don't know how long the path is, but it could extend to the bottom of the left subtree.
- The path starts at the root and goes down through the root's right child. 
Very similar to the previous case, but the direction is toward the right.
- The path involves both the left and the right child.
- The path doesn't involve any child. The root itself is the only element 
of the path with maximum sum.

To find the maximum path sum, we determine if 
there is a viable path leading down through the left or the right subtree. 
Please remember that a node can have negative or positive values. 
So a path sum contributed by a subtree could also be negative or positive. 
It would make sense to consider a path sum contributed by a subtree only if it is positive. 
If not, we can safely ignore it. 
In other words, the path goes down the left or the right subtree 
only if we see a gain in the path sum.

First determine the gain in the path sum 
contributed by the left and the right subtree.
Once we have both, we decide whether to include their contribution. 
=> Process the children before we process a node. 
=> Post-order traversal of the tree (children before parent)

Time: O(n). Each node in the tree is visited only once. 
During a visit, we perform constant time operations, 
including two recursive calls and calculating the max path sum for the current node.

Space: O(n). the recursive call stack can go as deep as the tree's height. 
In the worst case, the tree is a linked list, so the height is nnn.
"""
class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        # post order traversal of subtree rooted at `node`
        

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            #base case, if a node doesn't have left or right child
            #then the path sum contributed by the respective subtree is 0
            if not node: 
                return 0

            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gain_from_left = max(gain_from_subtree(node.left), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            """The path sum gain contributed by the subtree can be derived from a path 
            that includes at most one child of the root. 
            The root is already connected to its parent. 
            So if we include both children as well, with three connections, it wouldn't be a valid path anymore. 
            Therefore, we can say that the path would consist of at most one child of the root."""
            # return the max sum for a path starting at the root of subtree
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return max_path
    
"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

====
The serialization of a BST is essentially to encode
its values and more importantly its structure.
=> Tree Traversal

Approach 1: BFS
We scan through the tree level by level, following the order of height,
from top to bottom. The nodes on higher level would be visited before
the ones with lower levels.

Approach 2: DFS
We adopt the depth as the priority, so that one
would start from a root and reach all the way down to certain leaf,
and then back to root to reach another branch.

In this task, however, the DFS strategy is more adapted for our needs,
since the linkage among the adjacent nodes is naturally encoded in the order,
which is rather helpful for the later task of deserialization.

Time: O(n) -> visit each node exactly once
Space: O(n)
"""

# Pre-order DFS
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# BFS
class Codec:
    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res
            
    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root

"""
428. Serialize and Deserialize N-ary Tree
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in 
the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. 
An N-ary tree is a rooted tree in which each node has no more than N children. 
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

=====
Approach: BFS
BFS for serializing the tree and when deserializing 
=> construct one level at a time. 

The two main pieces of information that have to be infused in the serialized string are:
    - Which node has what children: since a level can contain a lot nodes 
and we need to know the parent of each one of them.
    - The switch from one level to another: will later help the deserializer know 
that a level has finished and a new one has begun.

For the first piece, we will be using a sentinel value of $ 
and whenever we start adding children of a different node, 
we add this sentinel value to the string and then start adding the children. 

For the next piece of information, we add another sentinel # to the string. 
Before we switch to the next level of the tree during serialization, 
we add this sentinel value to the string so that the deserializer knows that 
one level has ended and a new one has started. 

====
Algorithm:
Serialization
1. Make use of a queue here for traversing the tree one level at a time.
2. Perform a normal level order traversal. 
Add the childNode to the queue whenever done adding the children of a node to the queue.
3. When a particular level ends, we add an endNode to the queue.
4. Only when we pop a sentinel node from the queue 
do we add the corresponding characters to the final serialized string.
5. As for the nodes in the tree, use the unicode character trick we've been following all along.

Deserialization
1. Go one level at a time for reconstructing the tree.
2. Maintain two lists currentLevel and prevLevel. 
The prevLevel contains the nodes from the previous level 
while we add the nodes on the current level to the corresponding list. 
Once we have these two lists figured out, we establish the corresponding connections.
3. The sentinel values come in handy since whenever we encounter a $, 
the child switch sentinel, we pop a new parent node from prevLevel 
and any children encountered from this point to the next $ belong to this parent node.
4. Similarly, whenever we encounter the level end sentinel #, 
we assign prevLevel to currentLevel since the nodes in the current level 
now become parents for the next level.
"""

import collections 

class Codec:

    def _serializeHelper(self, root, serializedList):

        queue = collections.deque() 
        queue.append(root)
        queue.append(None)
        
        while queue:
            
            # Pop a node
            node = queue.popleft()
            
            # If this is an "endNode", we need to add another one
            # to mark the end of the current level unless this
            # was the last level.
            if (node == None):
                
                # We add a sentinal value of "#" here
                serializedList.append('#')
                if queue:
                    queue.append(None);  
                    
            elif node == 'C':
                
                # Add a sentinal value of "$" here to mark the switch to a
                # different parent.
                serializedList.append('$')
                
            else:
                
                # Add value of the current node and add all of it's
                # children nodes to the queue. Note how we convert
                # the integers to their corresponding ASCII counterparts.
                serializedList.append(chr(node.val + 48))
                for child in node.children:
                    queue.append(child)
                
                # If this not is NOT the last one on the current level, 
                # add a childNode as well since we move on to processing
                # the next node.
                if queue[0] != None:
                    queue.append('C')
        
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        if not root:
            return ""
        
        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)
        
    def _deserializeHelper(self, data, rootNode):
        
        # We move one level at a time and at every level, we need access
        # to the nodes on the previous level as well so that we can form
        # the children arrays properly. Hence two arrays.
        prevLevel, currentLevel = collections.deque(), collections.deque()
        currentLevel.append(rootNode)
        parentNode = rootNode
        
        # Process the characters in the string one at a time.
        for i in range (1, len(data)):
            if data[i] == '#':
                
                # Special processing for end of level. We need to swap the
                # array lists. Here, we simply re-initialize the "currentLevel"
                # arraylist rather than clearing it.
                prevLevel = currentLevel
                currentLevel = collections.deque()
                
                # Since we move one level down, we take the parent as the first
                # node on the current level.
                parentNode = prevLevel.popleft() if prevLevel else None;
                
            else:
                if data[i] == '$':
                    
                    # Special handling for change in parent on the same level
                    parentNode = prevLevel.popleft() if prevLevel else None;
                else:
                    childNode = Node(ord(data[i]) - 48, []);    
                    currentLevel.append(childNode)
                    parentNode.children.append(childNode)
                   
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data:
            return None
        
        rootNode = Node(ord(data[0]) - 48, [])
        self._deserializeHelper(data, rootNode)
        return rootNode
    
"""
199. Binary Tree RIght Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

====
Approach 1: BFS 
-> Why: return a list of last elements from EACH LEVEL  

Approach 2: DFS
to traverse the tree level by level, starting each time from the rightmost child.

"""
# DFS from right to left
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def getRight(root, curr_lvl):
            if not root:
                return 

            # if the length of the result (aka the number of levels that we traversed 
            # and added rightmost member of) > the current level, 
            # it means that we already processed this level 
            # and won't need to add anything else from this level
            if len(result) == curr_lvl:
                result.append(root.val)
            
            curr_lvl += 1
            getRight(root.right, curr_lvl)
            getRight(root.left, curr_lvl)

        getRight(root, 0)

        return result

# BFS
from collections import deque  

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []  # If the tree is empty, return an empty list

    result = []  # To store the right-side view elements
    queue = deque([root])  # Initialize a deque (double-ended queue) with the root node

    while queue:
        level_size = len(queue)  # Get the number of nodes at the current level

        for i in range(level_size):
            node = queue.popleft()  # Remove the node at the front of the queue

            if i == level_size - 1:
                # If this is the last node in the current level, add its value to the result
                result.append(node.val)

            # Add child nodes to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result  # Return the list of right-side view elements

"""
1359. Count All Valid Pickup and Delivery Options
Given n orders,each order consists of a pickup and a delivery service.

Count all valid pickup/delivery possible sequences such that delivery(i) is 
always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

eg: 
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

======================================================================
Approach 0: Brute Force - Recursive backtracking (TLE error)
Recursively explore every valid pickup and delivery option.
- Iterating over all of the orders
- For each order, if it is not picked up, pick up the order, mark the order as picked up, 
and make another recursive call. 
- If the order is already picked up but not delivered, 
then deliver the order and mark it as delivered. 
- After delivering all packages, we return from the recursive call 
and unmark the deliveries and pickups so that we can use them in another combination. 
=> recursive backtracking algorithm.
=> Not optimal 

=======
Approach 1: Recursion with Memoization (Top-Down DP)
In backtracking approach, we pick up each order one by one 
in order to generate all valid combinations. 
Since the problem asks us "count all valid pickup/delivery sequences," 
we can count the number of combinations without actually generating them.

If there are n unpicked orders, then we have n different options for orders that
we can pick up at the current step. So instead of picking up each order one by one 
and making a recursive call for each one, we could count the number of ways
to pick (n−1) unpicked orders and multiply it by the number of choices at the current step, n.
=> Improved from calling n times to only once
Same idea for delivering orders.

Base case: Finish delivering all orders -> found 1 way -> return 1.

Subproblems:
- If we want to pick one order, there are 'unpicked' different choices to pick at the current step. 
//waysToPick = unpicked * totalWays(unpicked - 1, undelivered)

- If we want to deliver one order, there are 'undelivered' - 'unpicked' 
(orders which are picked but not delivered) different choices.
//waysToDeliver = (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)

Edge case: unpicked > undelivered -> not make new recursive call -> return 0

Some subproblems are overlapping -> caching the result of each subproblem 
-> Memoization: create a data structure that we will use to cache results

========
Apporach 2: Tabulation (Bottom-up DP)
The top-down DP (recursive) requires some time and space to maintain a function call stack 
-> use bottom-up DP (iterative)

In the recursive approach, the variables that change are the number of unpicked and undelivered orders. 
-> each state in our DP table will be some combination of values for unpicked and undelivered.

dp[unpicked_num][undelivered_num]: the number of ways to arrange 'unpicked_num' unpicked and 'undelivered_num' undelivered orders.

Base case: All orders are picked and delivered -> 0 unpicked and 0 undelivered
-> there is one way to arrange the 0 remaining orders -> dp[0][0] = 1

Approach 3: Permutations (Math)
n orders each with a pickup and delivery -> 2n empty positions
1. First place all the n pickups in some random order (bc no constraints on placing pickups)
=> 1*2*...*n = n! ways

2. Placing deliveries one by one
=> 1*3*5*...*(2n-1) ways

"""
#Recursion with memoization (Top-down DP) => O(n^2) time, O(n^2) space
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        memo = [[0] * (n+1) for i in range(n+1)] #cache result of each subproblem

        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                # We have completed all orders.
                return 1

            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                # We can't pick or deliver more than N items
                # Number of deliveries can't exceed number of pickups 
                # as we can only deliver after a pickup.
                return 0

            if memo[unpicked][undelivered] != 0:
                #return cached value, if already present
                return memo[unpicked][undelivered]

            # Count all choices of picking up an order.
            ans = unpicked * totalWays(unpicked - 1, undelivered)
            ans %= MOD

            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)
            ans %= MOD

            memo[unpicked][undelivered] = ans
            return ans
        
        return totalWays(n, n)

#Tabulation (Bottom-up DP) => O(n^2) time, O(n^2) space
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):
                # If all orders are picked and delivered then,
                # for remaining '0' orders we have only one way.
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                
                # There are some unpicked elements left. 
                # We have choice to pick any one of those orders.
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                # Number of deliveries done is less than picked orders.
                # We have choice to deliver any one of (undelivered - unpicked) orders. 
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        
        return dp[n][n]

#Permutations => O(n) time, O(1) space
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, n + 1):
            # Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i
            # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1)
            ans %= MOD
        
        return ans
    
"""
1235. Maximum Profit in Job Scheduling
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], 
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, 
return the maximum profit you can take such that there are no two jobs in the subset 
with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

====================================================================================
Brute force idea:
For each job, there are two options, either to schedule it or not. 
The total number of possible combinations with N jobs is 2^n.
The brute force approach is to enumerate every possible combination.

Key notes:
1. A job cannot be scheduled if a conflicting job has already been scheduled. 
In other words, each decision we make is affected by the previous decisions we have made
2. The problem asks us to maximize the profit by scheduling non-conflicting jobs
=> Dynamic programming

======
Approach 1: Top-down DP + Binary Search

For each job, need to find the first non-conflicting job as the next job 
=> Use binary search instead of iterating: 
    1. Sort our jobs according to start time
    2. Binary search for the endTime of the next job in the list of start times for all jobs.

For each job, we will try two options:
    1. Schedule this job and move on to the next non-conflicting job using binary search.
    2. Skip this job and move on to the next available job.

The recursive approach will have repeated subproblems 
=> Memoization: Store maxProfit gained from the jobs from a position p to the end of the array

======
Approach 2: Bottom-up DP + Binary Search
dp[i]: max profit taking jobs start at interval i 

Base case: start from position=n because no more job to schedule -> max profit=0
Traverse the jobs array from right to left and build up memo with the previously calculated maximum profits. 
For each index, check the profit for 2 possible choices
    - If we schedule the job at index i, binary search to find the index (nextIndex) of the first non-conflicting job. 
The total profit by scheduling the job at index i is the sum of the profit of the current job and the value of dp[nextIndex].
    - If we skip the job at index i, the maximum profit will be the same as dp[i+1],
which is the maximum profit that can be obtained by starting at the next job.

Algorithm:
1. Store the startTime, endTime and profit of each job in jobs.
2. Sort the jobs according to their starting time.
3. Iterate over the jobs from right to left find the currProfit for each job. 
currProfit is the sum of the current job's profit and the maximum profit obtained by scheduling jobs between nextIndex and the end of the jobs array(dp[nextIndex]).
For each index i, set dp[i] equal to the maximum between currProfit and dp[i+1]. 
    - If currProfit is greater, then it's more profitable to schedule the job at index i, 
    - otherwise, it's better not to schedule this job.
4. Return the value dp[0].

=========
Possible follow-ups:
FOLLOW UP 1: Get the jobs you selected

In the DP array, instead of just storing max profit for a given index, also store which intervals led to that max profit. 
This will be either be [currInterval, nextAvailableInterval], or [nextImmediateInterval] 
-- since these are the 2 choices we made in the DP solution.

You can follow through the indices and collect which values were used. 
If the current index is in the list of intervals used, add it to the solution. 
Continue checking for the remaining index in the list.
-> O(n)

FOLLOW UP 2: Scale for n orders

Run the scheduler once -> remove the jobs that yield max profit  
-> run the scheduler a second time with the remaining jobs -> remove the jobs -> ... -> 
-> repeat until we get k overlaps

"""

#Bottom-up DP
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit)) #sort by start time

        #binary search to find the next non-conflicting job
        def find_next_job(i):
            l, r = i + 1, len(jobs) - 1
            while l <= r:
                m = (l + r) // 2
                if jobs[i][1] <= jobs[m][0]:
                    r = m - 1
                else:
                    l = m + 1
            return l

        n = len(jobs)
        dp = [0] * (n + 1)  

        for i in range(n - 1, -1, -1): 
            j = find_next_job(i)

            dp[i] = max(dp[i + 1], dp[j] + jobs[i][-1])

        return dp[0]  


"""
826. Most Profit Assigning Work
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, 
then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

======
Approach: Sort + 2 Pointers
1. Sorting: 
The algorithm starts by sorting the jobs based on their difficulty and the workers based on their ability. 
Sorting the jobs allows us to process them in ascending order of difficulty, 
making it easier to find jobs that each worker can handle. 
Sorting the workers ensures that we allocate jobs to workers with lower abilities first.

2. Two-Pointer Approach: 
The use of two pointers, i and j, allows us to efficiently match workers with jobs. 
Pointer i iterates through the sorted jobs, while pointer j iterates through the sorted workers. 
This approach helps us consider each worker's capability and maximize their profit.

3.Maximizing Profit for Each Worker: 
For each worker, we iterate through the sorted jobs list 
while the job's difficulty is within the worker's capability. 
During this process, we keep track of the maximum profit achievable for that worker. 

======
Time: O(nlogn)
"""

def maxProfitAssignment(difficulty, profit, worker):
    jobs = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
    #sort the job difficulty and worker ability in ascending order
    jobs.sort()
    worker.sort()
    
    i, j = 0, 0
    max_profit = 0
    temp_profit = 0
    
    while j < len(worker):
        #iterate through jobs to find the most difficult/profitable job for a worker
        while i < len(jobs) and jobs[i][0] <= worker[j]:
            temp_profit = max(temp_profit, jobs[i][1])
            i += 1
        max_profit += temp_profit #update max profit
        j += 1
    
    return max_profit

"""
2444. Count Subarrays with Fixed Bounds
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

eg: 
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

=============================================================
Brute Force Idea: Iterate over each subarray and check if its min and max value are minK and maxK

Approach: 2 Pointers
** Count how many valid subarrays end at i
Record three indexes:
    - leftBound: the most recent value out of the range [minK, maxK],
    - maxPosition: the most recent index with value equal to maxK.
    - minPosition: the most recent index with value equal to minK.

Let smaller = min(minPosition, maxPosition), 
so the range [smaller, i] contains at least one minK and one maxK. 
Now we try to extend the subarray [smaller, i] from the left side ([smaller - 1, i], [smaller - 2, i] etc.), 
which we can do as long as we haven't met a value out of the range.

However, we don't need to really extend the subarray but 
just record the index of the most recent value that is out of the range (leftBound), 
then the number of valid subarrays ending at i equals smaller - leftBound
If leftBound is to the right of smaller, smaller - leftBound brings a negative result, 
which means that there is no valid subarray, so we can just treat the result as 0 to avoid negative values. 

Algorithm
1. Initialize three indices minPosition, maxPosition and leftBound as -1 and set answer as 0.
2. Iterate over nums, for each index i:
    - If nums[i] is out of the range [minK, maxK], update leftBound = i.
    - If nums[i] equals minK, update minPosition = i.
    - If nums[i] equals maxK, update maxPosition = i.
    - The number of valid subarrays ending at index i equals min(minPosition, maxPosition) - leftBound. 
If the result is negative, it means there is no valid subarray ending at i. 
    - Increment answer by the number of valid subarrays.
3. Return answer once the iteration stops.

===========================================
Time: O(n)

"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        answer = 0
        min_position = max_position = left_bound = -1
        
        # Iterate over nums, for each number at index i:
        for i, number in enumerate(nums):
            # If the number is outside the range [minK, maxK], update the most recent left_bound.
            if number < minK or number > maxK:
                left_bound = i
                
            # If the number is minK or maxK, update the most recent position.
            if number == minK:
                min_position = i
            if number == maxK:
                max_position = i
                
            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            answer += max(0, min(min_position, max_position) - left_bound)
            
        return answer

"""
1347. Minimum Number of Steps to Make 2 Strings Anagram
You are given two strings of the same length s and t. 
In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

================
Approach: Hashmap 
1. Count the character frequency of each string, put in Hashmap/Counter 
2. For each character compare the frequency in 2 strings and calculate the number of steps needed to modify:
    - If the character in string t is present in string s and appears more times in t than s, 
then we replace some occurrences of this character in t to match the frequency in s. 
    - If the character in string t is not present in s, 
then all occurrences of this character in t need to be replaced. 

"""
from collections import Counter

def minSteps(s: str, t: str) -> int:
    # Count character frequency in 2 strings
    s_count = Counter(s)
    t_count = Counter(t)

    # Compare the character frequencies and calculate the steps needed.
    diff = 0
    for char, freq in t_count.items():
        if char in s_count and freq > s_count[char]:
            # Calculate the difference in frequency
            diff += (freq - s_count[char]) 
        elif char not in s_count:
            # If a character in s is not in t, all occurrences need to be changed.
            diff += freq
        
    return diff

"""
658. Find K Closest Elements
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    - |a - x| < |b - x|, or
    - |a - x| == |b - x| and a < b

====================================================================
Approach: Binary search to find left bound

Key observation: only either mid or mid+k could possibly be in a final answer. 
=> If the element at arr[mid] is closer to x than arr[mid + k], 
then that means arr[mid + k], as well as every element to the right of it can never be in the answer. 
This means we should move our right pointer to avoid considering them. 
The logic is the same vice-versa - if arr[mid + k] is closer to x, then move the left pointer.
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        #at this point, left is the smallest element satisfying the condition
        return arr[left:left + k]


"""
759. Employee Free Time
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, 
also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals,
not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, 
and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, 
as they have zero length.

==================
Approach: 
1. Sort all intervals by start time
2. Merge all intervals
3. Find the gap in merged list -> common free time

==================
Time: O(nlogn)

"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # combine all employee schedule
        intervals = []
        for employee_schedule in schedule:
            intervals.extend(employee_schedule)

        # sort the full schedule by start time
        intervals.sort(key=lambda interval: interval.start)

        # find the common free time
        free_time = []
        prev_end = intervals[0].end
        for interval in intervals:
            # if curr interval starts after prev_end
            # aka we found a free time, add the free time
            # that starts with prev_end and ends with curr_start
            if interval.start > prev_end:
                free_time.append(Interval(prev_end, interval.start))
            
            #update prev_end 
            prev_end = max(prev_end, interval.end)
        
        return free_time


""""
224. Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3
===========================================================================
Approach: Stack
Key: using "-" as a magnitude for the operands, we just have one operator left 
which is addition and + is associative.
e.g. A−B−C could be re-written as A+(−B)+(−C)

"""
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        # After processing all characters, add any remaining number
        return res + sign * operand

"""
329. Longest Increasing Path in a Matrix
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

=================================================================
Approach: DFS + Memoization
Cache[x][y]: store the length of the longest increasing path starting from cell [x][y]

1. Traverse each cell in matrix, initialize max_length value
2. DFS on neighboring cells, add and update max_length, store max_length in cache

"""
def longestIncreasingPath(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Define a recursive DFS function with memoization
    def dfs(x, y, matrix, cache):
        if cache[x][y] != -1:
            return cache[x][y]

        max_length = 1  # Initialize max_length to 1 for the current cell

        # Explore the four possible directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if the new cell is within bounds and has a greater value
            if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                # Recursively call dfs and add 1 for the current cell to extend the path
                length = 1 + dfs(new_x, new_y, matrix, cache)
                max_length = max(max_length, length)

        # Memoize the result for the current cell
        cache[x][y] = max_length
        return max_length

    max_length = 0
    # Initialize a memoization matrix with -1 for all cells
    cache = [[-1] * n for _ in range(m)]

    # Iterate through each cell and find the longest increasing path
    for i in range(m):
        for j in range(n):
            length = dfs(i, j, matrix, cache)
            max_length = max(max_length, length)

    # Return the maximum path length found
    return max_length

"""
239. SLiding Window Maximum
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
==================================================================

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        for i in range(len(nums)):
            # Remove elements that are out of the current window
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements smaller than the current element
            while window and nums[i] >= nums[window[-1]]:
                window.pop()

            # Add the current index to the window
            window.append(i)

            # Add the maximum element to the result if we have a complete window
            if i >= k - 1:
                result.append(nums[window[0]])

        return result

"""
286. Walls and Gates
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

=====================================================================
Approach: BFS
Multi-source BFS from all gates simultaneously
BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1, 
the distance to an empty room must be the shortest.
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        kInf = 2**31-1
        rows=len(rooms)
        cols=len(rooms[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        
        #first find gates and append to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c,0)) #row,col,distance
        
        #start bfs to find empty room at each level of distance from gates
        while queue:
            r,c,dist = queue.popleft()
            #explore 4 directions, append to queue
            for d in dirs:
                new_r, new_c = r+d[0], c+d[1]
                if 0 <= new_r < rows and 0 <= new_c < cols and rooms[new_r][new_c] == kInf:
                    rooms[new_r][new_c] = dist+1
                    queue.append((new_r,new_c,dist+1))
