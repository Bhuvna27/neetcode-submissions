class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        h_map = {}
        
        for i in range(len(nums)):
            if target-nums[i] not in h_map:
                h_map[nums[i]]=i
            else:
                return [h_map.get(target-nums[i]), i]
            


        