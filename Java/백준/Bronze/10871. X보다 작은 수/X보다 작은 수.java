import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        input = br.readLine();
        st = new StringTokenizer(input);
        int[] a = new int[n];
        for (int i=0; i<n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        for (int number : a) {
            if (number < x) {
                sb.append(number).append(" ");
            }
        }

        bw.write(sb.toString());
        bw.flush();
    }
}