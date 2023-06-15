import java.util.*;
public class level31{
    public static String solution(String x, String y) {
        // Your code here
        long a = Long.parseLong(x);
        long b = Long.parseLong(y);
        long c = 0L;
        if (a==1 || b==1){
            if (b==1)
                return String.valueOf(a-1);
            else return String.valueOf(b-1);
        }
        else{
            if (a>b){
                c = a/b;
                a = a%b;
            }
            else{
                c = b/a;
                b = b%a;
                //System.out.println("The c value is: "+c);
            }
        }
        while (a>0 && b>0){
            if (a>b){
                a-=b;
            }
            else{
                b-=a;
            }
            c++;
            //System.out.println("The c value is: "+c);
            if (a==1 && b==1)
                return String.valueOf(c);
        }
        if (a!=1 && b!=1)
            return "impossible";
        return String.valueOf(c);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String x = sc.nextLine();
        String y = sc.nextLine();
        String ans = solution(x, y);
        System.out.println(ans);
        sc.close();
    }
}