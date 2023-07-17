class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a = []
        a.append(first)
        for i in range(len(encoded)):
            a.append(encoded[i]^a[i])
        return a
        