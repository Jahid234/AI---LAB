import numpy as np

def createSudokuBoard():
    board = [
            [3, 0, 0, 1],
            [0, 1, 3, 2],
            [0, 0, 2, 3],
            [0, 0, 0, 4]
        ]
    
    board = np.array(board)
    return board


class Sudoku:
    
    def isValidBoard(self, brd):
        
        for x in range(4):
            
            rowList = brd[x, :]
            if (0 in rowList):
                rowList = np.delete(rowList, np.where(rowList == 0))
            
            colList = brd[:, x]
            if (0 in colList):
                colList = np.delete(colList, np.where(colList == 0))
            
            if x == 0:
                i, j = 0, 0
            elif x == 1:
                i, j = 0, 2
            elif x == 2:
                i, j = 2, 0
            elif x == 3:
                i, j = 2, 2
                
            subgridList = np.ravel( brd[i:i+2, j:j+2] )
            if (0 in subgridList):
                subgridList = np.delete(subgridList, np.where(subgridList == 0))

            if ( len(set(rowList)) != len(rowList)
                or len(set(colList)) != len(colList)
                or len(set(subgridList)) != len(subgridList)
            ):
                return False
        return True



if __name__ == "__main__":
    brd = createSudokuBoard()
    print (brd)
    
    ob = Sudoku()
    temp = ob.isValidBoard(brd)
    if temp:
        print ("Valid Board")
    else:
        print ("Invalid Board")

