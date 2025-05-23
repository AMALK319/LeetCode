class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = ""
                while(stack and stack[-1] != "["):
                    temp = stack.pop() + temp
                stack.pop()
                k = ""
                while(stack and stack[-1].isdigit()):
                    k = stack.pop() + k
                stack.append(temp*int(k))
        return "".join(stack)


        
            
           


        