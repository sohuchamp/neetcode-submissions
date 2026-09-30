class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0] * (2*len(nums))
        k = 0
        for i in range(len(newNums)):
            if k == (len(nums)):
                print("k is being reset")
                k = 0
            print(f"k is {k} and value in nums is {nums[k]}")
            newNums[i] = nums[k]

            k +=1

        return newNums
        
        