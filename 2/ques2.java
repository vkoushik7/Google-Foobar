import java.util.Arrays;
import java.util.ArrayList;

public class ques2 {
    public static String sub(String s, int base) {
        char[] sar = s.toCharArray();
        Arrays.sort(sar);
        String a = new String(sar);
        String b = new StringBuilder(a).reverse().toString();
        int n1 = Integer.parseInt(b, base);
        int n2 = Integer.parseInt(a, base);
        return Integer.toString(n1 - n2, base);
    }

    public static int solution(String n, int b) {
        // Your code here
        ArrayList<String> ls = new ArrayList<>();
        int ans = 0;
        while (7 > 0) {
            n = sub(n, b);
            if (ls.contains(n))
                break;
            ls.add(n);
            ans += 1;
        }
        return ls.size() - ls.indexOf(n);
    }
}