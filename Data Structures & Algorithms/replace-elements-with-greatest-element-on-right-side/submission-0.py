class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # sudo algorithm
        """
        Take the current value you are in in the array
        And then iterate from the end of the array, to the point
        you are at, and find the max value, and then store that 
        max value where you are at
        """

        

        for i in range(len(arr)):
            maxValue = 0

            for j in range(len(arr)-1, i, -1):

                if arr[j] > maxValue:
                    maxValue = arr[j]
                    
            arr[i] = maxValue
        arr[-1] = -1
        return arr
                


