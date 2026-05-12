class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        int[] new_array = new int[num_list.length + 1];
        for (int i = 0; i < num_list.length; i++) {
            new_array[i] = num_list[i];
        }
        if (num_list[num_list.length-2] < num_list[num_list.length-1]) {
            new_array[new_array.length - 1] = num_list[num_list.length - 1] - num_list[num_list.length - 2];
        } else {
            new_array[new_array.length - 1] = num_list[num_list.length - 1] * 2;
        }
        answer = new_array;
        return answer;
    }
}