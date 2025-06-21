class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        strs.sort()
        n = len(strs[0])
        for i in range(n):
            if strs[-1][i] != strs[0][i]:
                return longest
            longest += strs[0][i]
        return longest