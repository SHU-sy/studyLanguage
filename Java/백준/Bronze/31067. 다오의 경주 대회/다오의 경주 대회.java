import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        long k = Long.parseLong(st.nextToken());

        long[] tracks = new long[(int) n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            tracks[i] = Long.parseLong(st.nextToken());
        }

        int count = 0;

        for (int i = 1; i < n; i++) {
            if (tracks[i-1] >= tracks[i]) {
                if (tracks[i-1]-tracks[i] < k) {
                    count++;
                    tracks[i] += k;
                }
                else {
                    System.out.println(-1);
                    System.exit(0);
                }
            }
        }
        System.out.println(count);
    }
}