class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNumberMap = {} # hashMap{value: index}
        for i, v in enumerate(nums): 
            diff = target - v
            if diff in prevNumberMap: 
                return [prevNumberMap[diff], i] # returning the solution
            prevNumberMap[v] = i # updating the map if is not the solution 
        return 