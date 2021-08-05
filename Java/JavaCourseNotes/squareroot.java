public class squareroot {
    public static void main(String[] args) {
        double EPS = 1E-15; // error tolerence (15 places)
        double c = Double.parseDouble(args[0]);
        double t = c;
        double pi = Math.PI;

        while (Math.abs(t - (c/t)) > t*EPS) {
            t = ((c/t) + t) / 2.0;
        }

        System.out.println(t);
        System.out.println(pi);

    }
}
