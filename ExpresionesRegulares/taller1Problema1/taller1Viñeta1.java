package ExpresionesRegulares.taller1Problema1;
import java.io.*;
import java.util.*;
import java.util.regex.*;

/**
 * taller1Viñeta1
 */
public class taller1Viñeta1 {
    public static void main(String[] args) {
        String patron = "^123[123]*321$|12321";
        Pattern regex = Pattern.compile(patron); //creacion del patron
        //el que buscara coincidencias
        Scanner inputScanner = new Scanner(System.in);
        String cadena = inputScanner.nextLine();

        Matcher coincideMatcher =  regex.matcher(cadena);
        if(coincideMatcher.matches()){
            System.out.println("ACEPTA");
        }else{
            System.out.println("RECHAZA");
        }
    }
}