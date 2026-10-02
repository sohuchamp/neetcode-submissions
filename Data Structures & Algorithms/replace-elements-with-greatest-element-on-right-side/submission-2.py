class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = -1
        for i in range(len(arr)-1, -1, -1):
            curValue = arr[i]
            arr[i] = maxValue
            if curValue > maxValue:
                maxValue = curValue
        return arr 



            
                


