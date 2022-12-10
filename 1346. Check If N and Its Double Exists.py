class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        countofzero = 0
        for i in arr:
            if i == 0:
                countofzero += 1
        if countofzero > 1:
            return True
        count = set(arr)
        if countofzero == 1:
            count.remove(0)
        for i in count:
            if i * 2 in count:
                return True
        return False
