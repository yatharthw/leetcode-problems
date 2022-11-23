# first approach
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = []
        for i in board:
            horizontal.append(dict(Counter(i)))
        vertical = []
        for i in range(9):
            emp = {}
            for row in board:
                if row[i] in emp:
                    emp[row[i]] += 1
                else:
                    emp[row[i]] = 1
            vertical.append(emp)
        box = []
        i, j = 0, 0
        while i < 9:
            j = 0
            while j < 9:
                emp = {}
                # 1
                if board[i][j] in emp:
                    emp[board[i][j]] += 1
                else:
                    emp[board[i][j]] = 1
                # 2
                if board[i][j+1] in emp:
                    emp[board[i][j+1]] += 1
                else:
                    emp[board[i][j+1]] = 1
                # 3
                if board[i][j+2] in emp:
                    emp[board[i][j+2]] += 1
                else:
                    emp[board[i][j+2]] = 1
                # 4
                if board[i+1][j] in emp:
                    emp[board[i+1][j]] += 1
                else:
                    emp[board[i+1][j]] = 1
                # 5
                if board[i+1][j+1] in emp:
                    emp[board[i+1][j+1]] += 1
                else:
                    emp[board[i+1][j+1]] = 1
                # 6
                if board[i+1][j+2] in emp:
                    emp[board[i+1][j+2]] += 1
                else:
                    emp[board[i+1][j+2]] = 1
                # 7
                if board[i+2][j] in emp:
                    emp[board[i+2][j]] += 1
                else:
                    emp[board[i+2][j]] = 1
                # 8
                if board[i+2][j+1] in emp:
                    emp[board[i+2][j+1]] += 1
                else:
                    emp[board[i+2][j+1]] = 1
                # 9
                if board[i+2][j+2] in emp:
                    emp[board[i+2][j+2]] += 1
                else:
                    emp[board[i+2][j+2]] = 1
                box.append(emp)
                j += 3
            i += 3
        
        for i in vertical:
            for j in i:
                if j!= '.' and i[j] > 1:
                    return False
        for i in horizontal:
            for j in i:
                if j!= '.' and i[j] > 1:
                    return False
        for i in box:
            for j in i:
                if j!= '.' and i[j] > 1:
                    return False
        return True
