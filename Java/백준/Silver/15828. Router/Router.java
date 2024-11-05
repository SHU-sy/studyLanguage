import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        Queue<Integer> router = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());

        while (true) {
            int packet = Integer.parseInt(br.readLine());

            if (packet == -1) {
                break;
            }

            else if (packet == 0) {
                router.poll();
            }

            else {
                if (router.size() >= n){
                    continue;
                }
                else{
                    router.add(packet);
                }
            }
        }

        if (router.isEmpty()) {
            sb.append("empty");
        } else {
            while (!router.isEmpty()) {
                sb.append(router.poll()).append(" ");
            }
        }

        bw.write(sb.toString().trim());
        bw.flush();
    }
}