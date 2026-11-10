class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}


        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        
        for letter in t:
            if letter in counts:
                counts[letter] -= 1
            else:
                return False
        for value in counts.values():
            if value > 0:
                return False
        return True


        

        


        
        
        
        