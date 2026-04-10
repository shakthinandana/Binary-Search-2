# // Time Complexity :  O(log n)
# // Space Complexity :  O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Thinking of edge cases took attempts

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        if nums[low] < nums[high]: return nums[low]
        if high==0: return nums[0]

        while(low <= high):
            mid = low+ (high-low)//2

            if nums[mid] > nums[mid+1] : return nums[mid+1]
            if nums[mid-1] > nums[mid] : return nums[mid]

            if nums[low] < nums[mid] : low = mid+1
            else: high = mid-1