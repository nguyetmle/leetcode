/**
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
    represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
    
    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
    and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
 */

//level: medium
//approach: merge newInterval when start of intervals[i] <= end of newInterval, then add newInterval
//          add the original intervals[i] when end of intervals[i] < start of newInterval & the remainings after comparing


class InsertInterval {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        //initialize an array list of int[] to hold result
        List<int[]> ans = new ArrayList<>();
        int i = 0;

        //if end of intervals[i] < start of newInterval
        while (i<n && intervals[i][1] < newInterval[0]) 
            ans.add(intervals[i]); //add to result list
            i++;

        //if start of intervals[i] <= end of newInterval
        //intervals[i] overlaps with newInterval
        while (i<n && intervals[i][0] <= newInterval[1]) {
            //merge newInterval with intervals[i]
            newInterval[0] = Math.min(newInterval[0],intervals[i][0]); //choose the smaller start
            newInterval[1] = Math.max(newInterval[1],intervals[i][1]); //choose the bigger end
            i++;
        }
        ans.add(newInterval); //add newInterval to result list

        //add the remainings
        while (i<n)
            ans.add(intervals[i++]);
        
        return ans.toArray(new int[ans.size()][]);
    }
}