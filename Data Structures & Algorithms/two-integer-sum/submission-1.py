class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h_map = {}
        
        for i in range(len(nums)):
            if target-nums[i] not in h_map:
                h_map[nums[i]]=i
            else:
                return [h_map.get(target-nums[i]), i]
            


        