class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        k = 0
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
            
        return False
        

          

            

        

            
            


        
        

        
        