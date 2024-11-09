import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        int[] h = new int[n];
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            h[i] = Integer.parseInt(st1.nextToken());
        }

        Arrays.sort(h);

        for (int i = 0; i < n; i++) {
            if (h[i] > l) {
                break;
            }
            l += 1;
        }
        System.out.println(l);
    }
}