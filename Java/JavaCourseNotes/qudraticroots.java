///// To find out roots of the equation :-
/////            ax^2 + bx + c (given a, b, c)

public class qudraticroots {
    public static void main(String[] args) {
        
        // Parsing the coefficients of x^2 , x , constant
        double a = Double.parseDouble(args[0]),
        b = Double.parseDouble(args[1]),
        c = Double.parseDouble(args[2]);
        
        // calculating the roots according to the formula

        double descrimnent = b * b - 4.0 * c;
        double d = Math.sqrt(descrimnent);
        double root1 = (-b + d) / (2 * a);
        double root2 = (-b - d) / (2 * a);

        System.out.println("The roots for the given coefficients of the equation are : " + root1 + " and " + root2 + ".");
    }
}
