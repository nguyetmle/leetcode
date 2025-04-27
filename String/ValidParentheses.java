/**
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
 */

// level: easy
// approach: use stack 

import java.util.*;

class ValidParentheses {
    public boolean isValid(String s) {
        //initialize stack to store closing brackets
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            //if c is an opening bracket, push the corresonding closing bracket to stack
            if (c == '(') 
                stack.push(')');
            else if (c == '{')
                stack.push('}')
            else if (c == '[')
                stack.push(']')
            //if c is a closing bracket, pop the stack
            //c should match stack.pop() to be valid
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }

        //if stack is empty, it means all closing brackets are popped out and all parentheses are matching
        //else, parentheses are not matching
        return stack.isEmpty();
    }
}