package OrientacionAObjetos;

public class GestionaEquipo {

	public static void main(String[] args) {

		Persona p1= new Persona ("Andrea", "Perea", "12345678c"); 
		Persona p2 = new Persona ("Luis", "Perea", "12345679d"); 
		Persona p3 new Persona("David", "Perez", "22345678c"); 
		Persona p4 new Persona ("Sebastián", "Rodríguez", "28145678c");
		
		Persona[] personas1 = {p1,p2};
		Persona[] personas2 = {p3,p4};
		int [] puntuaciones1 = {7,14,22};
		int [] puntuaciones2 = {40,12,3};
		
		Equipo equipo1 = new Equipo("equipo1", puntuaciones1, personas1);
		System.out.println(equipo1);
		Persona[] tablaPersonas = equipo1.personas;
		for (int i=0; i< tablaPersonas.lenght; i++)
		{
			Persona p= tablaPersonas [i];
			System.out.println(p.dni);
		}
		Equipo equipo2 = new Equipo("equipo2", puntuaciones2, personas2);
		
		
	}

}
