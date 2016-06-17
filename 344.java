public class Solution {
    public String reverseString(String s) {
        if (s.length() == 0) {
            return "";
        }
        int n = s.length();
        char[] t = s.toCharArray();
        for (int i=0; i<n/2; i++) {
            char temp = t[i];
            t[i] = t[n-i-1];
            t[n-i-1] = temp;
        }
        return new String(t);
    }
}