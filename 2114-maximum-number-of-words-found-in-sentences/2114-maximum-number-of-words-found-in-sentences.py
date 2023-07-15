class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x = []
        for a in sentences:
            x.append(len(a.split()))
        return max(x)
    
        