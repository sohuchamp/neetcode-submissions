class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # sudo algorithm
        """
        Take the current value you are in in the array
        And then iterate from the end of the array, to the point
        you are at, and find the max value, and then store that 
        max value where you are at (brute force)

        A non brute force could operate on O(n). Iterate from the 
        right side right away, keep track of what the max value 
        and store it in the current i value
        """

        

        maxValue = -1
        for i in range(len(arr)-1,-1, -1 ):
            currentValue = arr[i]
            arr[i] = maxValue
            if currentValue > maxValue:
                maxValue = currentValue

        return arr
            



            
                


