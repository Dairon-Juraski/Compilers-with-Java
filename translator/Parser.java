package compiler.translator;

import java.io.IOException;

/**
 *
 * @author juraski
 */
public class Parser {

    static int lookahead; // Reading head

    public Parser() throws IOException {
        System.out.print("Input:");
        lookahead = System.in.read(); // Expression reading
    }

    private void match(int t) throws IOException {
        if (lookahead == t) {
            lookahead = System.in.read();
        } else {
            throw new Error("syntax error");
        }
    }

    private void term() throws IOException {
        if (Character.isDigit((char) lookahead)) {
            System.out.print((char) lookahead);

            match(lookahead);
        } else {
            throw new Error("syntax error");
        }
    }

    public void expr() throws IOException {
        int aux = Character.getNumericValue((char) lookahead); // primeiro caractere 
        term();
        while (true) // search for mathematical operations
        {
            switch (lookahead) {
                case '*':
                    match('*');
                    aux *= Character.getNumericValue((char) lookahead);
                    term();
                    System.out.println("*: " + aux);
                    break;
                case '/':
                    match('/');
                    aux /= Character.getNumericValue((char) lookahead);
                    term();
                    System.out.println("/: " + aux);
                    break;
                case '+':
                    match('+');
                    aux += Character.getNumericValue((char) lookahead);
                    term();
                    System.out.println("+: " + aux);
                    break;
                case '-':
                    match('-');
                    aux -= Character.getNumericValue((char) lookahead);
                    term();
                    System.out.println("-: " + aux);
                    break;
                default:
                    System.out.println("\nResultado inteiro:" + aux);
                    return; // erro de sintaxe ou printa resposta                return;
            }
        }
    }
}