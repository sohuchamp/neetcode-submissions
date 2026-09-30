class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        if sortedT == sortedS:
            return True
        return False
        
        