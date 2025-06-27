class Solution(object):
    def firstUniqChar(self, word):
        freq_map = defaultdict(int)
        for c in word:
            freq_map[c] += 1
        
        for i in range(len(word)):
            if freq_map[word[i]] == 1:
                return i
        
        return -1
        