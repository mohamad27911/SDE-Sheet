class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums)-1 
        while i > 0 and nums[i] <=  nums[i-1] :# find first descreasing element :1,3,4,2 => 3 cz 3<4
            i-=1
        if i == 0:#if its sorted descending 
            nums.reverse()# 3,2,1 => 1,2,3
            return
        
        j = len(nums)-1
        while j >= i and nums[j] <=nums[i-1]:# Find the element just larger than nums[i - 1] => 4
            j-=1
        nums[i-1],nums[j] = nums[j],nums[i-1]# Swap the found elements : 1,3,4,2 ==> 1,4,3,2
        nums[i:]= reversed(nums[i:])# Reverse the elements to the right of i - 1: 1,4,3,2 ==> 1,4,2,3
        
