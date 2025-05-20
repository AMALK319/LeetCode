class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        map = {}
        double = ""
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1

        answer = ""

        for word in words:
            if word == word[::-1]:
                answer += word*(map[word]//2)
                if map[word]%2 != 0 :
                    double = word
            elif (word[::-1] in map):
                answer += word*min(map[word], map[word[::-1]])
            map[word] = 0

        reverse = answer[::-1]
        answer += double + reverse

        return len(answer)
 