import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> stu = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        int max_len = 0;
        int last_stu = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());

            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                stu.addLast(b);

                if (stu.size() > max_len) {
                    max_len = stu.size();
                    last_stu = b;
                }
                else if (stu.size() == max_len) {
                    last_stu = Math.min(b, last_stu);
                }
            }
            else {
                stu.pollFirst();
            }
        }

        if (max_len > 0) {
            sb.append(max_len).append(" ").append(last_stu);
        }
        else {
            sb.append("empty");
        }

        System.out.println(sb);
    }
}