import java.util.*;
public class level22{
    public static int[] solution(int[] pegs) {
        // Your code here
        int n = pegs.length;
        int d = 0;
        int c = 1;
        for (int i=0;i<n-1;i++){
            int k = pegs[i+1]-pegs[i];
            d += (c*k);
            c*=-1;
        }
        int ans[] = new int[2];
        if (d<=0){
            ans[0] = -1;
            ans[1] = -1;
            return ans;
        }
        d*=2;
        if (n%2==0){
            if (d%3==0){
                ans[0] = d/3;
                ans[1] = 1;
            }
            else{
                ans[0] = d;
                ans[1] = 3;
            }
        }
        else{
            ans[0] = d;
            ans[1] = 1;
        }
        return ans;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        int ans[] = solution(arr);
        for (int i=0;i<2;i++)
            System.out.print(ans[i]+" ");
        sc.close();
    }
}