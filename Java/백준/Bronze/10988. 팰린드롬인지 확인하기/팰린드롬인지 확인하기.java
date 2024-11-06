import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        StringBuilder sb = new StringBuilder(word);
        String reverse_word = sb.reverse().toString();

        System.out.println((word.equals(reverse_word)) ? 1 : 0);
    }
}