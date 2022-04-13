from pprint import pprint


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):

    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 

    # column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # square
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    #recursion
    
    row, col = find_next_empty(puzzle)

    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    for guess in range(1, 10): 
        # step 3: is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
        [5, 3, -1,   -1, 7, -1,   -1, -1, -1],
        [6, -1, -1,   1, 9, 5,   -1, -1, -1],
        [-1, 9, 8,   -1, -1, -1,   -1, 6, -1],

        [8, -1, -1,   -1, 6, -1,   -1, -1, 3],
        [4, -1, -1,   8, -1, 3,   -1, -1, 1],
        [7, -1, -1,   -1, 2, -1,   -1, -1, 6],

        [-1, 6, -1,   -1, -1, -1,   2, 8, -1],
        [-1, -1, -1,   4, 1, 9,   -1, -1, 5],
        [-1, -1, -1,   -1, 8, -1,   -1, 7, 9]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)