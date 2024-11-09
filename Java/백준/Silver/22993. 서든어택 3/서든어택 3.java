import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Long[] attack = new Long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            attack[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(attack, 1, n);
        Long a1 = attack[0];

        for (int i = 1; i < n; i++) {
            if (a1 > attack[i]) {
                a1 += attack[i];
            }
            else {
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");
    }
}