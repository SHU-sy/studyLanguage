import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int k = Integer.parseInt(br.readLine());

        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            int[] score = new int[n];
            for (int j = 0; j < n; j++) {
                score[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(score);
            for (int j = 0; j < score.length / 2; j++) {
                int temp = score[j];
                score[j] = score[score.length - 1 - j];
                score[score.length - 1 - j] = temp;
            }
            int largestGap = 0;
            for (int j = 0; j < score.length - 1; j++) {
                largestGap = Math.max(largestGap, score[j] - score[j + 1]);
            }

            sb.append("Class ").append(i+1).append("\n");
            sb.append("Max ").append(score[0]).append(", Min ").append(score[score.length - 1]).append(", Largest gap ").append(largestGap).append("\n");
        }
        System.out.println(sb);
    }
}