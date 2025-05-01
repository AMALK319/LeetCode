class Solution(object):
    def uniqueOccurrences(self, arr):
        map1 = {}
        map2 = {}
        
        for i in range(len(arr)):
            if(arr[i] in map1):
                map1[arr[i]] += 1
            else:
                map1[arr[i]] = 1
        
        for val in map1.values():
            if val in map2:
                return False
            map2[val] = 1
        
        return True