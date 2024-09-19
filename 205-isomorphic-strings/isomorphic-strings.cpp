class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.length();
        unordered_map<char, int> sChars, tChars;
        int counterS = 0;
        int counterT = 0;
        for (int i = 0; i < n; i++) {
            if (sChars.find(s[i]) == sChars.end()) {
                sChars[s[i]] = counterS;
                counterS++;
                
            }
            if (tChars.find(t[i]) == tChars.end()) {
                tChars[t[i]] = counterT;
                counterT++;
            }
            if (sChars[s[i]] != tChars[t[i]])
                return false;
        }
        return true;
    }
};