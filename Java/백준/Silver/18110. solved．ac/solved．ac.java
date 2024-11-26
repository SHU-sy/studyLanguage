import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n==0){
            System.out.println("0");
        }
        else {
            long[] scores = new long[n];

            for (int i = 0; i < n; i++) {
                scores[i] = Long.parseLong(br.readLine());
            }
            Arrays.sort(scores);

            int exception = (int) Math.round(n*0.15);
            long[] exception_score = new long[n-(2*exception)];
            for (int i = 0; i < n-(2*exception); i++) {
                exception_score[i] = scores[i+(2*exception)];
            }

            long sum = 0;

            for (int i = exception; i < n - exception; i++) {
                sum += scores[i];
            }

            double average = (double) sum / (n - 2 * exception);
            System.out.println(Math.round(average));
        }
    }
}