import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());
        int max_score = 0;

        for (int i=0; i<n; i++){
            int score = 0;
            for (int j=0; j<3; j++) {
                st = new StringTokenizer(br.readLine());
                int a1 = Integer.parseInt(st.nextToken());
                int b1 = Integer.parseInt(st.nextToken());
                int c1 = Integer.parseInt(st.nextToken());

                score += (a1*a) + (b1*b) + (c1*c);

                if (score >= max_score) {
                    max_score = score;
                }
                else {
                    continue;
                }
            }
        }

        sb.append(max_score);
        bw.write(sb.toString());
        bw.flush();
    }
}