import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = 1000 - Integer.parseInt(br.readLine());
        int[] coin  = {500, 100, 50, 10, 5, 1};
        int count = 0;

        for (int c : coin) {
            count += n / c;
            n %= c;
        }
        System.out.println(count);
    }
}