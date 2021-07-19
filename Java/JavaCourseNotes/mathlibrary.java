public class mathlibrary {
    public static void main(String[] args) {
        double a = Double.parseDouble(args[0]);
        double b = Double.parseDouble(args[1]);
        
        // Using Math Libraty Functions

        // double abs(double a) : finds out absolute value

        double result = Math.abs(a);
        System.out.println("Absolute of " + a + " = " + result);

        // double max(double a, double b) : finds out greater value

        System.out.println("Maximum between " + a + " and " + b + " = " + Math.max(a, b));

        // double min(double a, double b) : finds out smaller value

        System.out.println("Minimum between " + a + " and " + b + " = " + Math.min(a, b));

        // double sin(double a) : finds sine of a

        System.out.println("Sine of " + a + " = " + Math.sin(a));

        // double cos(double a) : finds cosine of a

        System.out.println("Cosine of " + a + " = " + Math.cos(a));

        // double tan(double a) : tangent of a

        System.out.println("Tangent of " + a + " = " + Math.tan(a));

        // double exp(double a) : exponential (e^a)

        System.out.println("Exponential of " + a + " = " + Math.exp(a));

        // double log(double a) : natural log(ln a)

        System.out.println("Natural Log(ln) of " + a + " = " + Math.log(a));

        // double pow(double a, double b) : raise a to bth power(a^b)

        System.out.println(a + " rasied to " + b + "th power = " + Math.pow(a, b));

        // long round(double a) : rounds to nearest integer

        System.out.println("Nearest Integer of " + a + " = " + Math.round(a));

        // double random() : random number between [0, 1]

        System.out.println("A random number is " + Math.random());

        // double sqrt(double a) : gives sqrt of a

        System.out.println("Square root of " + a + " = " + Math.sqrt(a));

    }
}
