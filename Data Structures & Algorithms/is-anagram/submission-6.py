class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = {}

        countsT = {}

        for letter in s:
            #print(f"At this point s is {countsS}")
            if letter in countsS:
                countsS[letter] += 1
            else:
                countsS[letter] = 1
        for letter in t:
            #print(f"At this point t is {countsT}")
            if letter in countsT:
                countsT[letter] += 1
            else:
                countsT[letter] = 1
        #print(f"S is {countsS}")
        #print(f"T is {countsT}")

        
        if countsS == countsT:
            return True
        else:
            return False



        
        
        
        