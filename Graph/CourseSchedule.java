/**
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.
 */

//level: medium
//approach: dfs, topological sort
//note: - this problem is equivalent to finding if a cycle exists in a DIRECTED graph. 
//      - if a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.


enum State { kInit, kVisiting, kVisited }
//An enum type is a special data type that enables for a variable to be a set of predefined constants. 
//The variable must be equal to one of the values that have been predefined for it.

class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses] //initialize an array of courses (which later store array lists of prereqs) - like an adjacency list
        State[] state = new State[numCourses] //initialize an array to store the state (visited/visiting) of each course

        for (int i=0; i<numCourses; i++) {
            graph[i] = new ArrayList<>(); //create an array list for the prerequisites of each course
        } 
        
        for (int[] p : prerequisites) {
            graph[p[1]].add(p[0]) //add prerequisites to the graph according to its indexing
        }
        
        //detect if graph has cycle
        //if the graph is disconnected, then get the dfs forest and check for a cycle in individual tree
        for (int i=0; i<numCourses; i++) {
            if (hasCycle(graph,i,state))
                return false;
        }

        return true;
    }


    //check if a connected graph started at vertex u has cycle or not using dfs

    //there is a cycle only if there is a back edge in graph
    //to detect a back edge, keep track of vertices currently 
    //in the recursion stack of function for dfs traversal
    //(i.e. it's currently marked as kVisiting). 
    //if a vertex is reached that is already in the recursion stack
    //then there is a cycle
    private boolean hasCycle(List<Integer>[] graph, int u, State[] state) {
        //u is the current vertex (also the index in graph)
        //graph hold an array of lists of adjacent vertices
        //eg: graph = [[1],[3]] means vertex 0 is adjacent to vertex 1 and vertex 1 is adjacent to vertex 3 
        //so graph[u] = [v] means [v] is at index u in graph and v is adjacent to u
        
        //base case for dfs
        if (state[u] == State.kVisiting) //if we visit u again while we are visiting neighbors (of neighbors) of u 
            return true; //then there is a cycle
        if (state[u] == State.kVisited)  //if we visit u again after it's marked visited
            return false; //it just means u is adjacent to 2 or more vertices, thus no cycle
        
        //dfs process
        state[u] = State.kVisiting; //first visit u
        //then visit all neighbors of one neighbor of u (before moving to the next neighbor)
        for (final int v : graph[u]) {
            if (hasCycle(graph,v,state))
                return true;
        } 
        //at this point, we have explored all neighbors (and neighbors of neighbors) of u
        state[u] = State.kVisited; //mark as visited

        return false;

    }
}