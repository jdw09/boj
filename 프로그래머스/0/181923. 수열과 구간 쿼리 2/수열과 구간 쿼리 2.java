class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] query : queries) {
            for (int i : arr) {
                if (query[0] <= i && i >= query[2] && i <= query[1]) {
                    answer[answer.length] = i;
                }
            }
        }
        return answer;
    }
}