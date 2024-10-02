class Solution(object):
    def maxSubArray(self, nums):
        current_sum,max_sum=0,-999999999999
        for num in nums:
            current_sum+=num
            max_sum=max(max_sum,current_sum)
            if current_sum<0:
                current_sum=0
        return max_sum