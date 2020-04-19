package compiler.translator;

import java.io.IOException;

/**
 *
 * @author juraski
 */
public class MainTranslator {

    public static void main(String[] args) throws IOException {
        System.out.println("Insira um argumento válido:");
        System.out.println("EX: '9+5-2'; '9*5-3'; etc..");
        System.out.println("IMPORTANT PS->\nWILL BE CALCULED FORM THE LEFT TO RIGH!! ");
        System.out.println("---------------------------");
        while (true) {
            Parser parse = new Parser();
            parse.expr();
            System.out.println("\n--------------------------- \n");
        }
    }
}