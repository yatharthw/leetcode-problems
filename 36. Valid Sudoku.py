# better approach
# using sets and string encoding
# Collect the set of things we see, encoded as strings. For example:
# '4' in row 7 is encoded as "(4)7".
# '4' in column 7 is encoded as "7(4)".
# '4' in the top-right block is encoded as "0(4)2".
# Scream false if we ever fail to add something because it was already added (i.e., seen before).
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if '(' + str(board[i][j]) + ')' + str(i) in check or str(j) + '(' + str(board[i][j]) + ')' in check or str(i//3) + '(' + str(board[i][j]) + ')' + str(j//3) in check:
                        return False
                    else:
                        check.add('(' + str(board[i][j]) + ')' + str(i))
                        check.add(str(j) + '(' + str(board[i][j]) + ')')
                        check.add(str(i//3) + '(' + str(board[i][j]) + ')' + str(j//3))
        return True

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
