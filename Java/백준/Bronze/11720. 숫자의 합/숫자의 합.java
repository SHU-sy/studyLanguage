import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        long total_sum = 0;

        String num = br.readLine();
        for(int i = 0; i < n; i++) {
            char ch = num.charAt(i);
            int number = ch - '0';
            total_sum += number;
        }

        bw.write(String.valueOf(total_sum));
        bw.flush();
    }
}