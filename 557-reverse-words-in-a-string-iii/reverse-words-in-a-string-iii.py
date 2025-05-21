class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        ans = []
        for word in splitted:
            ans.append(word[::-1])
        return " ".join(ans)