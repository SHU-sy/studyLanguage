import java.io.*;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        HashSet<Integer> num_set = new HashSet<Integer>();

        for (int i=0; i< 10; i++){
            int a = Integer.parseInt(br.readLine());
            num_set.add(a%42);
        }
        sb.append(num_set.size());
        bw.write(sb.toString());
        bw.flush();
    }
}