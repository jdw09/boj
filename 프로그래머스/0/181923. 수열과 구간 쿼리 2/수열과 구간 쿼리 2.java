class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];

        for (int q = 0; q < queries.length; q++) {
            int[] query = queries[q];
            int min = Integer.MAX_VALUE;

            for (int i = query[0]; i <= query[1]; i++) {
                if (arr[i] > query[2]) {
                    min = Math.min(min, arr[i]);
                }
            }

            answer[q] = min == Integer.MAX_VALUE ? -1 : min;
        }

        return answer;
    }
}