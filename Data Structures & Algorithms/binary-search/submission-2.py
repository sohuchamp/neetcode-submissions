class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) -1, nums, target)
    
    def binarySearch(self, left: int, right: int, nums: List[int], target: int):
        #Base case 1, when the element is not found
        if left > right:
            return -1
        middle = (left + right) // 2

        #Base case 2, when the middle equals the target
        if nums[middle] == target:
            return middle
        
        #recursive calls, when the target is either less than or greater than the middle, reduce the search space by half
        elif nums[middle] > target:
            return self.binarySearch(left, middle-1, nums, target)
        else:
            return self.binarySearch(middle+1, right, nums, target)
        
        
        
       