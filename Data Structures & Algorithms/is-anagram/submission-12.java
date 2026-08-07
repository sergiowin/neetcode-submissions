class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> S = new HashMap<>();
        
        for(char c : s.toCharArray()){
            S.put(c, S.getOrDefault(c, 0) + 1);
        }
        for(char c : t.toCharArray()){
            S.put(c, S.getOrDefault(c, 0) - 1);
        }
        for(int count : S.values()){
            if(count != 0){
                return false;
            }
        }
        return true;
    }
}
