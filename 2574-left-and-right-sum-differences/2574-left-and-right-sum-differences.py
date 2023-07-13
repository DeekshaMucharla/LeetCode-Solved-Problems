class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        b.append(0)
        a.append(0)
        for i in range(len(nums)-1):
            a.append(a[i]+nums[i])
        for j in range(len(nums)-1,0,-1):
            b.append(b[abs(j-(len(nums)-1))]+nums[j])
        b = b[::-1]
        for i in range(len(nums)):
            a[i] = abs(a[i] - b[i])
        

        return a