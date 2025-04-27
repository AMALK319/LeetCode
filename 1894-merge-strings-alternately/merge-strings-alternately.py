class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1) if len(word1) < len(word2) else len(word2)
        merged = []
        
        for i in range(n):
            merged.append(word1[i])
            merged.append(word2[i])        
        merged.append(word1[n:])
        merged.append(word2[n:])

        return "".join(merged)
        