class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()  # Sort the array
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                i += 2  # Skip over the pair
            else:
                return nums[i-1]  # Return the single number
        return nums[-1]  # If the single number is at the end, return the last element
