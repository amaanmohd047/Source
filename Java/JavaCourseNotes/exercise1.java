public class exercise1 {
    public static void main(String[] args) {
        // Problem 1 : Uniform random numbers. Write a program that prints five uniform random numbers between 0 and 1, their average value, and their minimum and maximum values. Use Math.random(), Math.min(), and Math.max().
        // Solution :
            
        double z = Math.random(), x = Math.random(), c = Math.random(),  v = Math.random(), b = Math.random();
        double average = (z + x + c + v + b) / 5;
        double minimum = Math.min(b, Math.min(v, Math.min(c, Math.min(z, x))));
        double maximum = Math.max(b, Math.max(v, Math.max(c, Math.max(z, x))));
        System.out.print("The numbers are : ");
        System.out.println(z + "" + x + "" + c + "" + v + "" + b);
        System.out.println("The average of the numbers is : " + average + ". And " + minimum + " is the minimum and " + maximum + " is the maximum of the numbers");


        // Problem 2 : Three-sort. Write a program that takes three integer command-line arguments and prints them in ascending order. Use Math.min() and Math.max().
        // Solution :

        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);
        int num3 = Integer.parseInt(args[2]);

        int min = Math.min(num3, Math.min(num2, num1));
        int max = Math.max(num3, Math.max(num2, num1));

        int mid = (num1 + num2 + num3) - (min + max);

        System.out.println("The ascending order is : " + min + " < " + mid + " < " + max);
    }
}
