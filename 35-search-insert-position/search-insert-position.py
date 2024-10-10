class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # array is sorted -> binary search -> O(logn)

        L = 0 # left pointer initial position is at 0 
        R = len(nums)-1 # rigth one is at last element 

        while L <= R: # until L and R pointers havent cross each other 
            M = (L+R)//2 # middle element index

            if target == nums[M]: 
                return M 
            if target > nums[M]: 
                L = M + 1 
            else: 
                R = M - 1 # update the right pointer
                
        return L # if the target not found







        
                
