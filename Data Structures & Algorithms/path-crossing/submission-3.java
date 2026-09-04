

class Solution {
    public record Point(int x, int y) {}

    public boolean isPathCrossing(String path) {
        int x = 0;
        int y = 0;
        
        Set<Point> visited = new HashSet<>();
        visited.add(new Point(x, y));

        for (char move : path.toCharArray()) {
            switch (move) {
                case 'N' -> y++;
                case 'S' -> y--;
                case 'E' -> x++;
                case 'W' -> x--;
            }

            // add() returns false if the set already contains the Point
            if (!visited.add(new Point(x, y))) {
                return true;
            }
        }

        return false;
    }
}