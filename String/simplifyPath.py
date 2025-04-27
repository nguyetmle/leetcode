"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, 
convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    - The path starts with a single slash '/'.
    - Any two directories are separated by a single slash '/'.
    - The path does not end with a trailing '/'.
    - The path only contains the directories on the path from the root directory to the target file or directory
(i.e., no period '.' or double period '..')
    - Return the simplified canonical path.

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Level: medium
Approach: stack

"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] #a stack to store all directory
        paths = path.split("/") #list of directories, split by "/"
        for directory in paths:
            if directory == ".." and stack: #if there is ".." and already has some directory in the stack
                stack.pop() #go up 1 level of directory 
            elif directory == "." or directory == "" or directory == "..": #if ".." is the first directory, then cant go up
                continue
            else:
                stack.append(directory)
        
        return "/" + "/".join(stack)