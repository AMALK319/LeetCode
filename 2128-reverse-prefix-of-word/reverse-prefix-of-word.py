class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        s = ""
        i = 0
        while i < len(word):
            stack.append(word[i])
            if word[i] == ch:
                while(stack):
                    s += stack.pop()
                break
            i += 1 
            
        return s + word[i+1:]  if i < len(word) else word  

    
