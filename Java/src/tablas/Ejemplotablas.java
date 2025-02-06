package tablas;

public class Ejemplotablas {

	public static void main(String[] args) {
		String [] diasSemanas= {"Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"};
		for (String dia : diasSemanas)
		{	
			System.out.println(dia);
		}
		
		for (int pos = 0; pos< diasSemanas.length;pos++)
		{	
			System.out.println(diasSemanas[pos]);
		}

	}
}
