from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)
        
        idx = 0

        for color in range(3):
            count = freq.get(color, 0)
            nums[idx: idx + count] = [color] * count
            idx += count

        return nums