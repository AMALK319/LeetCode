class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCounter = {}
        for word in words:
            wordsCounter[word] = wordsCounter.get(word,0) + 1
        res = list(wordsCounter.keys())
        res.sort(key=lambda word: (-wordsCounter[word], word))
        
        return res[:k]