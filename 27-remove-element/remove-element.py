class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        temp = []
        for i in range(len(nums)): 
            if nums[i] != val: 
                
                nums[k] = nums[i]
                k += 1
            
        return k
            
