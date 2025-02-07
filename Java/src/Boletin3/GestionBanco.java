package Boletin3;

import java.time.LocalDate;

public class GestionBanco {

	public static void main(String[] args) {

		Personas3 titular = new Personas3 ("12345678A", "Jose","Garcia", LocalDate.of(2004, 10, 12));
		
		Personas3 autorizado = new Personas3 ("12345678A", "Jose","Garcia", LocalDate.of(2004, 10, 12));
		
		CuentaBancaria cuenta = new CuentaBancaria(0.0, "ES123456789123456789123456789", titular);
		
		cuenta.setSaldo(100);
		
		cuenta.ingresarDinero(autorizado, 100);
		
		
		
	}

}
