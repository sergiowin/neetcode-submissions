class Solution {
    public record Point(int x, int y) {}
    public boolean isPathCrossing(String path) {
        int x = 0;
        int y = 0;
        Set<Point> seen = new HashSet<>();
        seen.add(new Point(x,y));
        
        for (char move : path.toCharArray()){
            if (move == 'N'){
                y++;
            }
            else if (move == 'S'){
                y -= 1;
            }  
            else if (move == 'E'){
                x += 1;
            }
            else if (move == 'W'){
                x -= 1;
            }    
            if (seen.contains(new Point(x,y))) {
                return true;
            } else {
                seen.add(new Point(x,y));
            }
        }
        return false;
    }
}