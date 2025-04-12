import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static Integer[][] dp = new Integer[42][2]; //피보나치 수열에서 1과 0의 개수를 저장할 2차원 리스트 생성(n에서의 0과 1개수)

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //스캐너

        //exception in thread main 에러를 피하기 위해 리스트 기본 값 지정(null pointer)
        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[1][0] = 0;
        dp[1][1] = 1;

        int num = sc.nextInt(); //입력 회수

        for (int i = 0; i < num; i++){ //num번 반복
            int n = sc.nextInt(); // n 입력
            fib(n); // 함수 실행 -> fib(28~34 line)
            System.out.println(dp[n][0] + " " + dp[n][1]); // 결과 출력
        }
    }



    static Integer[] fib(int n) {
        if (dp[n][0] == null || dp[n][1] == null) { //만약 배열의 n번쨰가 빈칸이라면(계산된 적 없다면)
            dp[n][0] = fib(n-1)[0] + fib(n-2)[0]; //피보나치 수열 계산(n = fib(n-1) + fib(n-1))
            dp[n][1] = fib(n-1)[1] + fib(n-2)[1]; // ``
        }
        return dp[n]; //결과값 리턴
    }
}