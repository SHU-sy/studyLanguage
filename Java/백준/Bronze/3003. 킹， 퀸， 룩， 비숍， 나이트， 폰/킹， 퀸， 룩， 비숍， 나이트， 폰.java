import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String chess = "112228";
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 6; i++) {
            int num = Integer.parseInt(st.nextToken());
            sb.append(chess.charAt(i) - num - '0').append(" ");
        }
        System.out.println(sb);
    }
}