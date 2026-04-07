class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int star = 1;
        int sum = 0;
        for (int i : num_list){
            star *= i;
            sum += i;
        }
        
        if (Math.pow(sum, 2) > star) {
            answer = 1;
        } else {
            answer = 0;
        }
        return answer;
    }
}