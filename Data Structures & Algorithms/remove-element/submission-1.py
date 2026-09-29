class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0

        for i in range(len(nums)):
            print(f"nums i is {nums[i]} and is equated to {val}")
            if nums[i] != val:
                print(f"nums[k] is {nums[k]} and that will be set to {nums[i]}")
                nums[k] = nums[i]
                k += 1
                
        return k


        
        
        



