public class factors {
    public static void main(String[] args) {
        long n = Long.parseLong(args[0]);
        long sum =2;
        // if (n > 1) {
            for (int i = 2; i <= sum; i++) {
                while (n % i == 0) {
                    n = (n / i);
                    System.out.println(i + " ");
                }
                sum *= i;
            }

        if (n > 1) System.out.println(n);
        else System.out.println();
        // }
        // else if (n == 1) {
        //     System.out.println("1");
        // }
        // else {
        //     System.out.println("Wrong Input");
        // }
    }
}
