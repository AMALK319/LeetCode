class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)  
        n = len(num_str)
        max_num = num  

        """ for i in range(n):
            for j in range(i + 1, n):
                num_list = list(num_str)  
                num_list[i], num_list[j] = num_list[j],num_list[i] 
                temp = int("".join(num_list))  
                max_num = max(max_num, temp)  
        return max_num  """

        num_list = list(num_str)  
        for i in range(n-1):
            max_index = i
            for j in range(n-1, i, -1):
                if num_list[j] > num_list[max_index]:
                    max_index = j
            if max_index != i:
                num_list[i], num_list[max_index] = num_list[max_index],num_list[i]
                return int("".join(num_list))
        return num