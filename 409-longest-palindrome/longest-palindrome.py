class Solution:
    def longestPalindrome(self, s: str) -> int:
        isOdd = False
        freqMap = {} 
        length = 0 
        for c in s:
            freqMap[c] = 1 + freqMap.get(c,0)  
        for freq in freqMap.values():
            if freq%2 != 0:
                isOdd = True
                length += freq - 1
            else:
                length += freq
        return length + 1 if isOdd else length