import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int[] num = new int[30];
        for (int i=0; i<28; i++){
            int n = Integer.parseInt(br.readLine());
            num[n-1] = 1;
        }

        for (int i=0; i<30; i++){
            if (num[i] == 0){
                sb.append(i+1).append("\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
    }
}