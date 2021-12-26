#   Diane Kim
#   CmpSc132, Spring 2021
#   Final Lab: Create a Sudoku Puzzle Class
#   Main

from Sudoku_Class import SudokuPuzzle

def main():
    Sudoku = SudokuPuzzle()
    Sudoku.setChart([[1, 2, 3, 6, 7, 8, 9, 4, 5],
                     [5, 8, 4, 2, 3, 9, 7, 6, 1],
                     [9, 6, 7, 1, 4, 5, 3, 2, 8],
                     [3, 7, 2, 4, 6, 1, 5, 8, 9],
                     [6, 9, 1, 5, 8, 3, 2, 7, 4],
                     [4, 5, 8, 7, 9, 2, 6, 1, 3],
                     [8, 3, 6, 9, 2, 4, 1, 5, 7],
                     [2, 1, 9, 8, 5, 7, 4, 3, 6],
                     [7, 4, 5, 3, 1, 6, 8, 9, 2]])
    for row in Sudoku.getChart():
        print(*row)
    Sudoku.validatePuzzle()

main()



