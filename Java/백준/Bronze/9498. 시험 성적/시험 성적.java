import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int score = Integer.parseInt(br.readLine());

        if (90 <= score){
            bw.write("A");
        }
        else if (80 <= score){
            bw.write("B");
        }
        else if (70 <= score){
            bw.write("C");
        }
        else if (60 <= score){
            bw.write("D");
        }
        else{
            bw.write("F");
        }
        bw.flush();
    }
}