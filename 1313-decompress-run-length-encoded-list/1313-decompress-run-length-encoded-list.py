class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        t = []
        # a = []
        # for i in range(0,len(nums),2):
        #     a.append(nums[i])
        # for r in range(len(nums)):
        #     if(r%2!=0):
        for i in range(0,len(nums),2):
            for j in range(0,nums[i]):
                t.append(nums[i+1])
        return t
            