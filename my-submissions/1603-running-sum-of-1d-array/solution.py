class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        running_sum = 0
        for num in nums:
            running_sum = running_sum + num
            sum_list.append(running_sum)
            
        return sum_list
