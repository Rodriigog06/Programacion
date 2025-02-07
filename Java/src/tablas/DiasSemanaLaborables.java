package tablas;

public class DiasSemanaLaborables {

	public static void main(String[] args) {
		String [] diasLaborales= {"Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"};
		int pos = 0;
		while (pos < diasLaborales.length)
			if (pos<5) {
				System.out.println("laborable" +diasLaborales[pos]);
			} else {
				System.out.println("festivo" +diasLaborales[pos]);
			}
			pos = pos + 1;
	}
// Esto es una prueba para github
}
