public class whileloop {
    public static void main(String[] args) {
        // Powers Of Two
        int n = Integer.parseInt(args[0]);
        int i = 0, value = 1;

        while (i <= n ) {
            i ++;
            System.out.println(value);
            value = value * 2;
        }
    }
}
