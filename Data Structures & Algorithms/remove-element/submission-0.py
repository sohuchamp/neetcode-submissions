class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        
        
        # Counting the amount of the value in each array

        counter = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter
            
        
        

        
       
        

        return counter

        



