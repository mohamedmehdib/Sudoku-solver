class Solution:
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == "." :
                    for k in range(1,10):
                        if self.validSquare(str(k) , j , i ) and self.validHorizantally(board, str(k) , i) and self.validVertically(board , str(k) , j):
                            board[i][j] = str(k)
                            break
                    if self.validSolved(board):
                        return True

    def validSolved(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return False
        return True
    def validSquare(self,num,x,y):
        if x < 3:
            finX = 3
        elif x < 6:
            finX = 6
        else:
            finX = 9

        if y < 3:
            finY = 3
        elif y < 6:
            finY = 6
        else:
            finY = 9

        miniBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]

        k = 0

        for i in range(finY-3 , finY):
            p = 0
            for j in range(finX-3 , finX):
                miniBoard[k][p]
                p += 1
            k += 1


        for i in range(3):
            for j in range(3):
                if num == miniBoard[i][j]:
                    return False
        return True


    def validHorizantally(self,board,num,y):
        for i in range(9):
            if num == board[y][i]:
                return False
        return True


    def validVertically(self,board,num,x):
        for i in range(9):
            if num == board[i][x]:
                return False
        return True



    def printBoard(self,board):
        for i in range(9):
            for j in range(9):
                if j%3 == 2 : 
                    print(board[i][j] , end="|")
                else:
                    print(board[i][j] , end=" ")
            print()
            if i%3 == 2 :
                print("- "*9)






sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


sol.solveSudoku(board)

sol.printBoard(board)