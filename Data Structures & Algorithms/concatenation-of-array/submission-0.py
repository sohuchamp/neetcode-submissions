class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0] * (2*len(nums))
        k = 0
        
        for i in range(len(nums)):
            newNums[k] = nums[i]
            k += 1
        print(newNums) 
        print(k)
        for j in range(len(nums)):
            newNums[k] = nums[j]
            k +=1
        return newNums

        
        