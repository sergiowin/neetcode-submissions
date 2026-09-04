class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        seen = set()
        seen.add((0,0))
        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            elif move == 'W':
                x -= 1
            if (x,y) in seen:
                return True
            seen.add((x, y))
        return False
