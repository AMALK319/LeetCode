class Solution(object):
    def topKFrequent(self, words, k):
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        
        res = []
        while len(res) < k:
            max_count = 0
            freq_word = ""
            for key, val in counts.items():
                if val > max_count:
                    freq_word = key
                    max_count = val
                elif val == max_count and freq_word > key:
                        freq_word = key
            counts.pop(freq_word)
            res.append(freq_word)
        return res

        