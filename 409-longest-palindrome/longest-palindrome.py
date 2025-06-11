class Solution:
    def longestPalindrome(self, s: str) -> int:
        isOdd = False
        freqMap = {} 
        length = 0 
        for c in s:
            freqMap[c] = 1 + freqMap.get(c,0)  
        for freq in freqMap.values():
            if freq%2 != 0 and not isOdd:
                isOdd = True
                length += freq
            elif freq%2 != 0 and  isOdd:
                length += freq - 1
            elif freq%2 == 0:
                length += freq
        return length