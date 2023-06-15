import java.util.*;
public class level1{
    public static String solution(String x) {
        // Your code here
        String fans = "";
        int n = x.length();
        for (int i=0;i<n;i++){
            char ch = x.charAt(i);
            if (ch>=97 && ch<=122){
                int k = (int)ch;
                if (k<=109){
                    int ans = k-97;
                    ans = 122-ans;
                    char c = (char)ans;
                    //System.out.print(c);
                    fans = fans+c;
                }
                else{
                    int ans = k-109;
                    ans=110-ans;
                    char c = (char)ans;
                    //System.out.print(c);
                    fans = fans+c;
                }
            }
            else{
                fans = fans+ch;
            }
        }
        return fans;
    }
    public static void main(String[] args) {
        String s;   
        Scanner sc = new Scanner(System.in);
        s = sc.nextLine();
        String ans = solution(s);
        System.out.println(ans);
        sc.close();
    }
}