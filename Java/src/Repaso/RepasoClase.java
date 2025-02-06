package Repaso;

import java.util.Scanner;

public class RepasoClase {

	public static void main(String[] args) {
		Scanner scanner = new scanner(System.in);
		System.out.println ("¿Cuantos numeros quieres considerar?");
		int numero = scanner.nextInt();
		Repasos f =new Repasos ();
		System.out.println("El resultado es:"+ f.pares(numero,scanner));
		
	}
		int pares (int numero,Scanner sc)
}
