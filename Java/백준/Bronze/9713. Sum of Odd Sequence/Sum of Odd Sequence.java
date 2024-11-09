import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int total = 0;
            for (int j = 1; j <= n; j++) {
                if (j % 2 != 0) {
                    total += j;
                }
            }
            sb.append(total).append("\n");
        }

        System.out.println(sb);
    }
}