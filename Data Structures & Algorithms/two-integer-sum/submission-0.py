class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for e in range(len(nums)):
            for f in range(e + 1, len(nums)):
                g = nums[e] + nums[f]
                if g == target:
                    l = [e, f]
                    return l       