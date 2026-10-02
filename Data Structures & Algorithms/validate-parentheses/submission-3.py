class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingType = ['(', '{', '[']
        closingType = [')', '}', ']']
        matching = {
            ")" : "(",
            "}" : "{",
            "]" : "["

        }
        if len(s) <= 1:
            return False

        for i in s:
            print(stack)
            if i in openingType:
                print(f"i here is opening type {i}")
                stack.append(i)
            elif i in closingType:
                print(f"i here is closing type {i}")
                if not stack:
                    return False
                top_element = stack[-1]
                print(f"Top element is {top_element}")
                print(f"Matching one is {matching[i]}")
                if top_element == matching[i]:
                    stack.pop()
                else:
                    print("They did not match")
                    return False

        
        return len(stack) == 0

                

        


        