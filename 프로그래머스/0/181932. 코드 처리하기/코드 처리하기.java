class Solution {
    public String solution(String code) {
        String answer = "";
        char[] charArrayCode = code.toCharArray();
        boolean mode = false;
        for (int idx = 0; idx < charArrayCode.length; idx++) {
            if (charArrayCode[idx] == '1') {
                mode = !mode;
            } else if (mode == false && idx % 2 == 0) {
                answer += charArrayCode[idx];
            } else if (mode == true && idx % 2 == 1) {
                answer += charArrayCode[idx];
            }
        }
        if (answer.equals("")) {
            answer = "EMPTY";
        }
        return answer;
    }
}