import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int r = 0;

        if(a==b && b ==c) {
            r = 10000 + a * 1000;
        }
        else if (a == b || b == c || a == c) {
            int s = (a == b || a == c) ? a : b;
            r = 1000 + s * 100;
        }
        else {
            int max = Math.max(a, Math.max(b, c));
            r = max * 100;
        }
        bw.write(String.valueOf(r));
        bw.flush();
    }
}