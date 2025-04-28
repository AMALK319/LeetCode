class Solution(object):
    def reverseVowels(self, s):
        l,r = 0,len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        word = list(s)

        while(l<r):
            if((word[l] in vowels)and(word[r] in vowels)):
                word[l],word[r] = word[r], word[l]
                l += 1
                r -= 1
            elif((word[l] in vowels)and(word[r] not in vowels)):
                r -= 1
            elif((word[l] not in vowels)and(word[r] in vowels)):
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(word)

     
        