public class bodmas {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]),
        num2 =Integer.parseInt(args[1]),
        num3 = Integer.parseInt(args[2]),
        num4 = Integer.parseInt(args[3]),
        num5 = Integer.parseInt(args[4]);

        float result = num5 * num4 / num2 + num3 - num1;
        System.out.println(result);
        // Order : / * + -
    }
}
