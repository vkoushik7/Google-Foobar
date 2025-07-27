class ques7 {
    public static int solution(int start, int length) {
        // Your code goes here.
        int ans = 0;
        for (int i = length; i >= 1; i--) {
            for (int j = 1; j <= i; j++)
                ans = ans ^ (start + j - 1);
            start = start + length;
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(solution(0, 3));
    }
}