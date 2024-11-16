import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> ball = new HashMap<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            if (command == 1){
                int x = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                ball.put(w, x);
            }

            else if (command == 2){
                int w = Integer.parseInt(st.nextToken());
                sb.append(ball.get(w)).append('\n');
            }
        }
        System.out.println(sb);
    }
}