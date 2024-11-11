import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> normal = new HashMap<>();
        HashMap<String, Integer> special = new HashMap<>();
        List<String> service = new ArrayList<>();

        for (int i = 0; i < a; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            String menu = st1.nextToken();
            int price = Integer.parseInt(st1.nextToken());
            normal.put(menu, price);
        }

        for (int i = 0; i < b; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            String menu = st2.nextToken();
            int price = Integer.parseInt(st2.nextToken());
            special.put(menu, price);
        }

        for (int i = 0; i < c; i++) {
            service.add(br.readLine());
        }

        Long normal_price = 0L;
        Long special_price = 0L;
        int service_count = 0;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String order = br.readLine();

            if (normal.containsKey(order)) {
                normal_price += normal.get(order);
            }
            else if (special.containsKey(order)) {
                special_price += special.get(order);
            }
            else if (service.contains(order)) {
                service_count += 1;
                if (service_count > 1) {
                    System.out.println("No");
                    return;
                }
            }
        }

        if (special_price > 0 && normal_price < 20000) {
            System.out.println("No");
        }
        else if (special_price + normal_price < 50000 && service_count > 0) {
            System.out.println("No");
        }
        else {
            System.out.println("Okay");
        }
    }
}