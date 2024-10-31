import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());

        bw.write((a * (b % 10))+"\n");
        bw.write((a * ((b / 10) % 10))+"\n");
        bw.write(a * (b / 100)+"\n");
        bw.write((a * b)+"\n");

        bw.flush();
    }
}