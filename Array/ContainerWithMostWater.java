/**
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
 */

// level: medium
// approach: 2 pointers, greedy
import java.util.*;

class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int ans = 0;
        int l = 0;
        int r = height.length - 1;

        //loop through the array with 2 pointers
        while (l<r) { 
            int minHeight = Math.min(height[l],height[r]); //height of the container is the smaller height between 2 lines
            ans = Math.max(ans, minHeight * (r-l)); //calculate the area of container
            
            //if height of left pointer is smaller, increment left pointer
            if (height[l] < height[r])  
                l++;
            //else, decrement right pointer
            else
                r--;
        }

        return ans;
    }
}