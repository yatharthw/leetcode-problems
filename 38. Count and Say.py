# count the occurences of the digits in the number and keep adding the count and current number untill the number is equal to the current
class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        current = num
        while n > 1:
            res = ""
            count = 0
            # print(num)
            current = num[0]
            for i in range(len(num)):
                if num[i] == current:
                    count += 1
                else:
                    res += str(count) + current
                    current = num[i]
                    count = 1
            res += str(count) + current
            num = res
            n -= 1
        return num
        
