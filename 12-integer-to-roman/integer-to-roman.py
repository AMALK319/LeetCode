class Solution(object):
    def intToRoman(self, num):
         return (self.intToRomanPartial((num//1000)*1000) + 
                self.intToRomanPartial(((num%1000)//100)*100) + 
                self.intToRomanPartial(((num%100)//10)*10) + 
                self.intToRomanPartial(num%10))

    
    def intToRomanPartial(self,num):
        str = ""
        map = {1:"I", 4:"IV", 5: "V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        if num == 0:
            return ""
        elif num in map:
            str += map[num]
        elif (num < 10 and num < 5):
            str += map[1] * (num%10)
        elif (num < 10 and num > 5):
            str += map[5] + self.intToRomanPartial((num%10)-5)
        elif (num < 100 and num < 50):
            str += map[10] * (num//10)
        elif (num < 100 and num > 50):
            str += map[50] + self.intToRomanPartial( num-50)
        elif (num < 1000 and num < 500):
            str += map[100] * (num//100)
        elif (num < 1000 and num > 500):
            str += map[500] + self.intToRomanPartial( num-500)
        else:
            str += map[1000] * (num//1000)
        return str


