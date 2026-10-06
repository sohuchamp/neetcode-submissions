class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        lookUp = [0,0]

        for i in range(len(nums)):
            for j in range(len(nums) -1, i, -1):
                sum = nums[j] + nums[i]
                if sum == target:
                    lookUp[0] = i
                    lookUp[1] = j
        
        return lookUp



       
             
            


            


        
        