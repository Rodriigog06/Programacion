package Boletin5;

public class Arquero extends Personajes {
	
	public Arquero(String nombre, int nivel, int hp) {
		super(nombre, nivel, hp, "Flecha");
	}
	public boolean esAtacado(Personajes p) {
	boolean atacado;
		if (p instanceof Mago)	
		atacado = true;
	 else {
		atacado = false;
	}
		return atacado;
	}
	public boolean esAtacado(Personajes p, int distancia) {
		boolean atacado;
		if (p instanceof Mago)	
			atacado = true;
		else if (p instanceof Caballero && distancia < 50) {
		atacado = true;
	}
		return atacado;
}
}
