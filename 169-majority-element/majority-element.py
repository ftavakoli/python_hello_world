class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track_dict = {}
        i = 0

        while i < len(nums): 
            #populating the dictionary
            # number is new encaunter 
            if nums[i] in track_dict: 
                track_dict[nums[i]] += 1
                i += 1 
            # number is not seen before
            else: 
                track_dict[nums[i]] = 1 #adding the new item
                i += 1 

        majority_element = max(track_dict, key=track_dict.get)
        return majority_element
                
