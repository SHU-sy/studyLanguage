import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String money = "25 10 5 1";
            int c = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(money);

            for (int j=0; j < 4; j++) {
                int change = Integer.parseInt(st.nextToken());
                int result = c/change;
                c %= change;
                sb.append(result).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}