import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        long num1 = Long.parseLong(st.nextToken());
        long num2 = Long.parseLong(st.nextToken());

        long a = Math.min(num1, num2);
        long b = Math.max(num1, num2);

        if (a==b || b-a==1) {
            sb.append(0).append("\n");
        }
        else {
            sb.append(b-a-1).append("\n");
            for (long i=a+1; i<b; i++) {
                sb.append(i).append(" ");
            }
        }

        System.out.println(sb);
    }
}