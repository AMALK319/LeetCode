class Solution(object):
    def mergeAlternately(self, word1, word2):
        n1, n2 = len(word1),len(word2)
        n = n1 if n1 < n2 else n2
        
        merged = []
        for i in range(n):
            merged.append(word1[i])
            merged.append(word2[i])        
        merged.append(word1[n:])
        merged.append(word2[n:])

        return "".join(merged)
        