class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = {} 
        for num in nums:
            if num in count_map:
                count_map[num] += 1
                return True
            else: 
                count_map[num] = 1
        return False

        

            
             

        