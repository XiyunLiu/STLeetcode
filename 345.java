public class Solution {
    public String reverseVowels(String s) {
        if (s.length()==0) {
            return "";
        }
        HashSet<Character> vowel = new HashSet<Character>();
        String letter_row = new String("aeiouAEIOU");
        char[] letter= letter_row.toCharArray();
        for (char v:letter) {
            vowel.add(v);
        }
        int i = 0;
        int j = s.length()-1;
        char[] t = s.toCharArray();
        while (i<j) {
            while (i<j && !vowel.contains(t[i])) {
                i++;
            }
            while (j>i && !vowel.contains(t[j])) {
                j--;
            }
            char tmp = t[i];
            t[i] = t[j];
            t[j] = tmp;
            i++;
            j--;
        }
        return new String(t);
    }
}