class Solution {
    public static boolean isUpper(char ch) {
        if (ch >= 65 && ch <= 90)
            return true;
        return false;
    }
    public static boolean isLower(char ch) {
        if (ch >= 97 && ch <= 122)
            return true;
        return false;
    }
    public boolean detectCapitalUse(String word) {
        char c = word.charAt(0);
        int len = word.length();
        if(isLower(c)) {
            for (int i = 1; i < len; i++)
                if (isUpper(word.charAt(i)))
                    return false;
            return true;
        }
        else {
            char prev, curr;
            for (int i = 2; i < len; i++) {
                prev = word.charAt(i-1);
                curr = word.charAt(i);
                if (isLower(curr) && isUpper(prev) || isLower(prev) && isUpper(curr))
                    return false;
            }
            return true;
        }
    }
}
