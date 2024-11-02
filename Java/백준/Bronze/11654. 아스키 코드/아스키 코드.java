import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String n = br.readLine();
        char c = n.charAt(0);
        sb.append((int) c);

        bw.write(sb.toString());
        bw.flush();
    }
}