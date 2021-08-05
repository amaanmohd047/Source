public class condition {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        int max = 0;
        
        if (a > b) {
            if (a > c) {
                max = a;
            }

            else if (c > b) {
                max = c;
            }
        }
        else {
            max = b;
        }


        System.out.println("The Greatest number is " + max);
    }    
}
