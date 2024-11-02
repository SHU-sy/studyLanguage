import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine().trim();
        int[] first_index = new int[26];

        for(int i=0; i<26; i++){
            first_index[i] = -1;
        }

        for(int i=0; i<s.length(); i++){
            char w = s.charAt(i);
            if(first_index[w-'a'] == -1) {
                first_index[w-'a'] = i;
            }
        }

        for(int i=0; i<26; i++) {
            sb.append(first_index[i]).append(' ');
        }

        bw.write(sb.toString());
        bw.flush();
    }
}