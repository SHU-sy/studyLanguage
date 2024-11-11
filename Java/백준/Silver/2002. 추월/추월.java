import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        LinkedList<String> enter = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            enter.add(br.readLine());
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            String car = br.readLine();
            if (!enter.getFirst().equals(car)) {
                count++;
            }
            enter.remove(car);
        }
        System.out.println(count);
    }
}