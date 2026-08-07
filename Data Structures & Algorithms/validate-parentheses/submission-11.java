class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] string = s.toCharArray();
        for (char a : string){
            
            if((a == '(' || a == '{' || a == '[')){
                stack.push(a);
            }  
            else if(a == ')' || a == '}' || a == ']'){
                    if(stack.isEmpty()){
                    return false;
                    }
                  
                    else{
                        char temp = stack.pop();
                            if((a == ')' && temp != '(')||(a == '}' && temp != '{')||(a == ']' && temp != '[')){
                                return false;
                            }
                    }
                
            }
        }
    return stack.isEmpty();
        }
}

    

