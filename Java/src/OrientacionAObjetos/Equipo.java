package OrientacionAObjetos;

import java.util.Arrays;

public class Equipo {
	String nombreEquipo;
	int [] puntuaciones;
	Personas[]personas;
	int edad;
	

	public Equipo(String nombreEquipo, int[] puntuaciones, Personas[] personas, int edad) {
		super();
		this.nombreEquipo = nombreEquipo;
		this.puntuaciones = puntuaciones;
		this.personas = personas;
		this.edad = edad;
	}
	

	@Override
	public String toString() {
		return "Equipo [nombreEquipo=" + nombreEquipo + ", puntuaciones=" + Arrays.toString(puntuaciones)
				+ ", participantes=" + Arrays.toString(personas) + ", edad=" + edad + "]";
	}
	float calculaMediaEdad()
	{
		float mediaEdad = 0f; 
		Personas [] tablaPersona = this.personas;
		for(Personas p: tablaPersona)
		{
			System.out.println(p.edad);
		}
		return mediaEdad;
	}
	
	

}
