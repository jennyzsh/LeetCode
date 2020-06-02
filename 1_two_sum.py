from typing import List

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                next = nums[j]
                if curr + next == target:
                    return [i, j]
        return []

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, v in enumerate(nums):
            if target - v in hashmap:
                return [hashmap[target - v], idx]
            else :
                hashmap[v] = idx



if __name__ == '__main__':
    solution = Solution()
    l = solution.twoSum_2([3,3], 6)
    print(l)