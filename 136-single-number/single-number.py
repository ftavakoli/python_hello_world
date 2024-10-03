class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # to meet the requirments we have to go with XOR logic... 

        single_num = 0 # n ^ 0 = n 
        for num in nums: 
            single_num = num ^ single_num
        return single_num




        # # time: O(nlog(n)), space: O(log(n))

        # nums.sort()  # Sort the array
        # i = 1
        # while i < len(nums):
        #     if nums[i-1] == nums[i]:
        #         i += 2  # Skip over the pair
        #     else:
        #         return nums[i-1]  # Return the single number
        # return nums[-1]  # If the single number is at the end, return the last element





