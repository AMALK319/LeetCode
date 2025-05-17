class Solution:
    def defangIPaddr(self, address: str) -> str:
        splitted = address.split('.')
        return "[.]".join(splitted)
        