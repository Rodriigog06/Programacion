package Boletin6;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		int [] sumaCifra (); 
		{
		int resultado =0;
		Scanner sc = new Scanner(System.in);
		System.out.println ("Dame un numero cuyas cifras quieras sumar");
		String num1 = sc.next();
		System.out.println("Dame el  numero de cifras a sumar");
		int num2 = sc.nextInt();
		if(datosValidos(num1,num2))
		{for (int i=0; i< num2; i++)
			{
			String cifra =Character.toString(num1.charAt(0));
			int numCifra = Integer.parseInt(cifra);
			resultado = resultado +numCifra;
		}
		}

	}

}
