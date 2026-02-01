class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Sort everything after the first element and pick the first two
        return nums[0] + sum(sorted(nums[1:])[:2])