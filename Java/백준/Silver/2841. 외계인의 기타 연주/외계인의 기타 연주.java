import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Stack<Integer>> lists = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            lists.add(new Stack<>());
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int count = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int line = Integer.parseInt(st1.nextToken());
            int num = Integer.parseInt(st1.nextToken());
            line -= 1;

            while (!lists.get(line).isEmpty() && lists.get(line).peek() > num) {
                lists.get(line).pop();
                count++;
            }

            if (!lists.get(line).isEmpty() && lists.get(line).peek() == num) {
                continue;
            }

            lists.get(line).push(num);
            count++;
        }
        System.out.println(count);
    }
}