class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r = len(board)
        c = len(board[0])
        
        def get_sur(i,j):
            output = []
            if i>0:
                output.append([i-1,j])
            if i<r-1:
                output.append([i+1,j])
            if j>0:
                output.append([i,j-1])
            if j<c-1:
                output.append([i,j+1])
            return output
        def find_word(board,word,row,col) -> bool:
            #to do find word
            if len(word) == 0:
                return True
            sur = get_sur(row,col)
            temp = board[row][col]
            board[row][col] = '@'
            for a,b in sur:
                if board[a][b] == word[0] and find_word(board, word[1:],a,b):
                    return True
            board[row][col] = temp
            return False
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and find_word(board, word[1:],i,j):
                    return True
        return False
        