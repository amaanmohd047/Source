// A gambler starts with $(stake) money and places $1 bids and has a goal
// // Outcome 1 (loss): Gambler goes broke with $0
// // Outcome 1 (win): Gambler reaches the goal
// // // Q1. How many bets until win or loss?
// // // Q2. What are the chances of winning?

public class GamblerRuinProblem {
    public static void main(String[] args) {
        // // One Aproach: 
        // Mante Carlo Simulation

        // Parsing the command line args
        int stake = Integer.parseInt(args[0]);
        int goal = Integer.parseInt(args[1]);
        int trials = 100;
        int wins = 0, bets = 0;

        for (int t = 0; t < trials; t++) {
            int cash = stake;
            while (cash > 0 && cash < goal) {
                if(Math.random() > 0.5) {
                    cash++;
                    bets++;
                }
                else { cash--; bets++; }
            }
            if (cash == goal) { wins++; }
        }

        System.out.println("Bets : " + bets);
        System.out.println("Win Percentage : " + wins + "%");
    }
}
