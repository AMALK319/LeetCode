class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """stack = []
        s = ""

        i = 0
        while i < len(word):
            stack.append(word[i])
            if word[i] == ch:
                break
            i += 1 

        while(stack):
            s += stack.pop()

        return s + word[i+1:]  if i < len(word) else word  """

        s = ""
        i=0
        while i < len(word):
            s += word[i]
            if word[i] == ch:
                break
            i += 1 
        return s[::-1] + word[i+1:] if i < len(word) else word
