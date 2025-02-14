package Boletin5;

public class Mago extends Personajes{
	public Mago(String nombre, int nivel, int hp) {
		super(nombre, nivel, hp, "Hechizo");
	}
	public boolean esAtacado(Personajes p) {
		
		return false;
	}

	public boolean esAtacado(Personajes p, int distancia) {
		
	return false;
	}
}
