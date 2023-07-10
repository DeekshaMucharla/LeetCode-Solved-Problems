class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        y = []
        r = []
        a = len(nums)-n
        for i in range(a):
            x.append(nums[i])
        for j in range(a,2*n):
            y.append(nums[j])
        for k in range(a):
            r.append(x[k])
            r.append(y[k])
        return r