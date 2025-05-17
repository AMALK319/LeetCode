class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for c in address:
            res += c if c != '.' else "[.]"
        return res
        