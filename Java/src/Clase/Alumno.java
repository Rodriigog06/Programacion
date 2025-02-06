package Clase;

public class Alumno {

	public static void main(String[] args) {

		Alumno pepe = new Alumno();
		pepe.nombre = "Pepe";
		pepe.dni = "12345678d";
		pepe.nota = 5;
		
		Alumno susana = new Alumno();
		susana.nombre = "Susana";
		susana.dni = "12555678d";
		susana.nota = 4;
		
		String cadenaPepe = pepe.pasoACadena();
		System.out.println(cadenaPepe);
		String cadenaSusana = susana.pasoACadena();
		System.out.println(cadenaSusana);
		
		boolean apruebaPepe = pepe.estaAprobado();
		System.out.println(apruebaPepe);
		
		boolean suspendeSusana = susana.estaSuspensa();
		System.out.println(suspendeSusana);
		
		

	}

}
