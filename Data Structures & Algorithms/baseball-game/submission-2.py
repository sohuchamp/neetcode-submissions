class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operationSum = 0
        record = []
        k = 0

        for i in operations:

            if i == "+":
                print(f"k when accesing + is {k}")
                operationSum = (record[k-1] + record[k-2])
                record.append(operationSum)
                k +=1
            elif i == "D":
                print(f"k when accessing D is {k}")
                print(f"{len(record)}")
                record.append(2*int(record[k-1]))
                k+=1
            
            elif i == "C":
                print(f"k when accesing C is {k}")
                record.pop()
                k -= 1

            else:
                print(f"k when appending normally is {k}")
                record.append(int(i))
                k +=1

        
        print(record)

        total = sum(record)

        return total
            
        



        