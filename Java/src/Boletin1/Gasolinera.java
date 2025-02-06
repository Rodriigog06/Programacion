package Boletin1;

public class Gasolinera {

	public static void main(String[] args) {
		do {
			System.out.println ("1. Asignar el coche a un surtidor y repostar");
			System.out.println ("2. Consultar el estado de surtidores");
			System.out.println ("3. Asignar precio al suritdor");
			System.out.println ("4. Recargar surtidor");
			System.out.println ("5. Cerrar y salir del programa");
			
			System.out.print("Elige una opcion:");
			opcion = input.nextInt();
			
			switch (opcion) {
			
			case 1:
				System.out.println ("Asignar surtifot seleccionado")
				break;
			case 2:
				System.out.println ("Consultar estado de surtidores");
				break;
			case 3:
				System.out.println ("Asignar precio al surtidor");
				break;
			case 4:
				System.out.println ("Recargar surtidor");
				break;
			case 5:
				System.out.println ("Cerrar y salir del programa");
					break;
			}
		}

	}

}
