public class forloop {
    public static void main(String[] args) {
        
        int val = Integer.parseInt(args[0]);
        int m = Integer.parseInt(args[1]);
        
        for( int i = 0; i < m; i++) {
            System.out.println(val);
            val = val * 2;
        }
    }    
}
