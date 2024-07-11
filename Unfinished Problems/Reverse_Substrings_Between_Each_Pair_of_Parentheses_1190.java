// 1190. Reverse Substrings Between Each Pair of Parentheses

public class Reverse_Substrings_Between_Each_Pair_of_Parentheses_1190 {
    
}




class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> charStack = new Stack<>();
        
        s = "((" + s + "))";
        
        String result = "";
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            if (charStack.empty() || s.charAt(i) != ')') {
                charStack.push(s.charAt(i));
            } else {
                StringBuilder temp = new StringBuilder();
                
                while (charStack.peek() != '(') {
                    temp.append(charStack.pop());
                }
                
                charStack.pop();
                
                result = temp.toString();
                
                for (int j = 0; j < temp.length(); j++) {
                    charStack.push(temp.charAt(j));
                }
            }
        }
        return result;
    }
}







// tried to optimize the solution, but fail the edge cases
class SolutionA {
    public String reversString(String s) {
        if (s.length() == 1) {
            return s;
        }
        int start = 0;
        int end = s.length() - 1;
        String resultStart = "";
        String resultEnd = "";
        while (start < end) {
            resultStart += s.charAt(end);
            resultEnd = s.charAt(start) + resultEnd;
            start++;
            end--;
        }
        if (s.length() % 2 == 1) {
            resultStart += s.charAt(start);
        }
        return resultStart + resultEnd;
    }

    public String reverseParentheses(String s) {
        int start = 0;
        int end = s.length() - 1;
        String resultStart = "";
        String resultEnd = "";

        while (start < end) {
            System.out.println(s.charAt(start) + " _ " + s.charAt(end));
            System.out.println(s);
            if (s.charAt(start) == '(' || s.charAt(start) == ')') {
                if (s.charAt(end) != '(' && s.charAt(end) != ')') {
                    while ((s.charAt(end) != '(' && s.charAt(end) != ')') && start < end) {
                        resultEnd = s.charAt(end) + resultEnd;
                        end--;
                    }
                }
                s = reversString(s.substring(start + 1, end));
                start = 0;
                end = s.length() - 1;
                continue;
                // s = reversString(s.substring(start, end));
            }
            if (s.charAt(end) == '(' || s.charAt(end) == ')') {
                while ((s.charAt(start) != '(' && s.charAt(start) != ')') && start < end) {
                    resultStart += s.charAt(start);
                    start++;
                }
                if (start >= end) {
                    break;
                }
                s = reversString(s.substring(start + 1, end));
                start = 0;
                end = s.length() - 1;
                continue;
            }
            resultStart += s.charAt(start);
            resultEnd = s.charAt(end) + resultEnd;
            start++;
            end--;
        }
        if (s.length() % 2 == 1) {
            resultStart += s.charAt(start);
        }
        return resultStart + resultEnd;
    }
}