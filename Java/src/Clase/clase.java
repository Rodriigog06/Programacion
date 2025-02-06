package Clase;

import java.util.Scanner;

public class clase {



		String nombre;
		int unidades;
		float precioventa;
		boolean hayQPedirStock () {
			boolean pedir = false;
			if (unidades <= 3) {
				pedir = true;
			}
			else {
				pedir = false;
			}
			System.out.println("¿Hay que pedir más stock del producto?: " + pedir);
			return pedir;
		}
		
		int aumentaUnidades (int aumentos, Scanner sc) {
			System.out.println("¿Cuantos quieres aumentar?": + pedir);
			aumentos = sc.nextInt();
			System.out.println("Las unidades actuales de dicho producto son :" + unidades);
		return unidades;
		}
		String pasaAcadena () {
			String cadena = "Las unidades actuales del producto es de :" + unidades;
			return cadena;
		}

	}

}
