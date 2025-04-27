"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Level: medium
Approach: backtracking, rmb to add 0 from the beginning path list
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def backtrack(start,path):
            if start == len(graph) - 1: #if reach target (node n-1), add to ans
                return ans.append(list(path))
            
            for node in graph[start]: #explore all nodes adjacent to start node
                path.append(node)
                backtrack(node,path)
                path.pop()
        
        backtrack(0,[0]) #start from source node 0
        return ans
