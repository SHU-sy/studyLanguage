import java.io.*;
import java.util.*;

class Res {
    int stu_len;
    int stu_last;

    Res(int stu_len, int stu_last) {
        this.stu_len = stu_len;
        this.stu_last = stu_last;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> stu = new ArrayDeque<>();
        List<Res> result = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());

            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                stu.addLast(b);
            }
            else {
                stu.pollLast();
            }

            if (!stu.isEmpty()) {
                result.add(new Res(stu.size(), stu.getLast()));
            }
        }

        result.sort(Comparator.comparing((Res r) -> r.stu_len).reversed()
                .thenComparing(r -> r.stu_last));

        if (!result.isEmpty()) {
            Res first = result.get(0);
            sb.append(first.stu_len).append(' ').append(first.stu_last);
        }
        else {
            sb.append("empty");
        }

        System.out.println(sb);
    }
}