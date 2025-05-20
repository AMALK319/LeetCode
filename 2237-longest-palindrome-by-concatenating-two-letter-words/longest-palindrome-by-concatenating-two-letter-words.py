class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        map = {}
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1

        answer = 0
        centred = False
        for word in words:
            backward = word[::-1]
            if word == backward:
                answer += 2*(2*(map[word]//2))
                if map[word]%2 != 0 :
                    centred = True
            elif (backward in map):
                answer += 2*(2*min(map[word], map[backward]))
            map[word] = 0

        if centred :
            answer += 2
        return answer
 