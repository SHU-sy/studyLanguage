import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] score = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            score[i] = Integer.parseInt(st.nextToken());
        }

        double m = Arrays.stream(score).max().orElse(0);
        double s = Arrays.stream(score).sum();

        sb.append(s*100/m/n);
        bw.write(sb.toString());
        bw.flush();
    }
}