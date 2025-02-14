package Boletin5;

import java.util.Objects;

public class Personajes {
	private String nombre;
	private int nivel;
	private int hp;
	private String arma;
	
	
	protected Personajes(String nombre, int nivel, int hp, String arma) {
		super();
		this.nombre = nombre;
		this.nivel = nivel;
		this.hp = hp;
		this.arma = arma;
	}


	protected String getNombre() {
		return nombre;
	}


	protected void setNombre(String nombre) {
		this.nombre = nombre;
	}


	protected int getNivel() {
		return nivel;
	}


	protected void setNivel(int nivel) {
		this.nivel = nivel;
	}


	protected int getHp() {
		return hp;
	}


	protected void setHp(int hp) {
		this.hp = hp;
	}


	protected String getArma() {
		return arma;
	}


	protected void setArma(String arma) {
		this.arma = arma;
	}
	
	public boolean esAtacado(Personajes p) {
		
		return false;
	}


	@Override
	public String toString() {
		return "Personajes [nombre=" + nombre + ", nivel=" + nivel + ", hp=" + hp + ", arma=" + arma + "]";
	}


	@Override
	public int hashCode() {
		return Objects.hash(arma, hp, nivel, nombre);
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Personajes other = (Personajes) obj;
		return Objects.equals(arma, other.arma) && hp == other.hp && nivel == other.nivel
				&& Objects.equals(nombre, other.nombre);
	}
	
	
	
	

}
