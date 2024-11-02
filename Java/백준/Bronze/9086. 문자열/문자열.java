import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++) {
            String word = br.readLine();
            sb.append(word.charAt(0)).append(word.charAt(word.length()-1)).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }
}