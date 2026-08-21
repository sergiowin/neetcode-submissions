class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## need to keep track of both row and column (0-indexed so 0-8 really)
        ## create hash sets for rows columns and 3x3 grids.
        ## check as iterating for early termination
        i = 0
        j = 0
        rows = defaultdict(set)
        columns = defaultdict(set) 
        grids = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                ##skip checks if this isn't a value
                if val == ".":
                    continue
                
                grid_key = (i//3, j//3)
                if val in rows[i] or val in columns[j] or val in grids[grid_key]:
                    return False
                rows[i].add(val)
                columns[j].add(val)
                grids[grid_key].add(val)
        return True