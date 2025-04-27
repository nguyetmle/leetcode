"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Level: medium
Approach: find the max number of overlapping intervals at any given time
"""
# [0,5,15]
# [10,20,30]
class Solution:
    def minMeetingRooms(self, intervals):
        # Separate out the start and the end timings and sort them individually.
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)

        s = e = 0
        used_rooms, res = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                # A new meeting is starting
                used_rooms += 1
                s += 1
            else:
                # A current meeting is ending
                used_rooms -= 1
                e += 1
            res = max(res, used_rooms)

        return res 