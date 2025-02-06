package Simulacro;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(system.in);
		int numDados, numApuesta;
		float dineroapuesta, dineroGanancias;
		String[] historico = new String[200];
		int numeroJugadas = 0;
		
		int opcion = imprimeMenu();
		while (opcion < 3)
		{
			switch (opcion) {
			case 1: {
				numApuesta = dameNumApuesta(sc);
				dineroApuesta = dameDineroApuesta();
				numDados = tirabaDadosYSuma();
				dineroGanancias = calculaGanancias(numApuesta, dineroApuesta, numDados);
				registrajugadaEnHistorico(historico, numDados, numApuesta, dineroApuesta);
			
				
			}
			}
		}
		
	
	}
	
}
