public class infiniteloop {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int i = 0, v = 1;

        while (n >= i) 
            System.out.println(v);
            i += 1;
            v *= 2;
    }
    
}
