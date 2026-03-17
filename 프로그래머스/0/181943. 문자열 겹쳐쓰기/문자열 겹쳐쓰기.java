class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder answer = new StringBuilder("");
        for (int i = 0; i < my_string.length(); i++) {
            if (s <= i && i < (overwrite_string.length() + s)) {
                answer.append(overwrite_string.charAt(i - s));
            } else {
                answer.append(my_string.charAt(i));
            }
        }
        return answer.toString();
    }
}