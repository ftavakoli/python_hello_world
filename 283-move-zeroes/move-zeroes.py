class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0  # Keep track of how many zeros we've found
        
        while i < len(nums) - zeros:  # Adjust the loop condition based on zero count
            if nums[i] == 0:
                nums.pop(i)      # Pop the zero at index i
                nums.append(0)   # Append zero to the end
                zeros += 1       # Increment zero count
            else:
                i += 1  # Only move to the next index if a non-zero is found
        # non_zero_pos = 0  # Pointer to track the position for non-zero elements
        
        # # Move non-zero elements to the front
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
        #         non_zero_pos += 1
        
        # # All remaining positions after the last non-zero element are set to 0

        