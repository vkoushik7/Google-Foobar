import java.util.*;
public class level21{
    public static int solution(String s) {
        //Your code here
        int c = 0;
        int n = s.length();
        int i = 0;
        while (s.charAt(i)=='<')
            i++;
        for (;i<n;i++){
            char ch = s.charAt(i);
            if (ch=='>'){
                for (int j=i+1;j<n;j++){
                    char chk = s.charAt(j);
                    if (chk=='<')
                        c++;
                }
            }
        }
        return c*2;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int ans = solution(s);
        System.out.println(ans);
        sc.close();
    }
}