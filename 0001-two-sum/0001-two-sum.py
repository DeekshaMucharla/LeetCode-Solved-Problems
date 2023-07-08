class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = len(nums)
        y = []
        for i in range(x):
            a = target-nums[i]
            for j in range(i+1,x):
                if(a==nums[j]):
                    y.append(i)
                    y.append(j)
        return y
                    