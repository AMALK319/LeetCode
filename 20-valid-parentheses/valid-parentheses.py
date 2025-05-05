class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in map.keys():
                stack.append(c)
            elif not stack or c != map.get(stack.pop()):
                return False
        return len(stack) == 0
        