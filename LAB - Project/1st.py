import numpy as np 

def createSudokuboard():     

    ## ... Initial 2D matrix    
    sudoku = np.array([[3, 0, 0, 1], [0, 1, 3, 2], [0, 0, 2, 3], [0, 0, 0, 4]])
    return sudoku    
    
if __name__ == "__main__":
    board = createSudokuboard()
    print(board)
    

