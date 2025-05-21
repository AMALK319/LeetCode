class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n, partitions = len(s), []
        for c in s:
            m = len(partitions)
            exists = False
            for i in range(m):
                if c in partitions[i]:
                    partitions[i] = "".join(partitions[i:]) + c
                    partitions = partitions[:i]+[partitions[i]]
                    exists = True
                    break
            if not exists:
                partitions.append(c)
        result = []
        for part in partitions:
            result.append(len(part))
        return result