package Boletin5oo;

public class Conductor {
	private String nombre;
	private int ano;
	
	protected Conductor(String nombre, int ano) {
		super();
		this.nombre = nombre;
		setAno(ano);
	}

	protected String getNombre() {
		return nombre;
	}

	protected void setNombre(String nombre) {
		this.nombre = nombre;
	}

	protected int getAno() {
		return ano;
	}

	protected void setAno(int ano) {
		if(ano>0) {
		this.ano = ano;
	}else { 
		this.ano = 0;
	}
	}
	
	@Override
	public String toString() {
		return "Conductor [nombre=" + nombre + ", ano=" + ano + "]";
	}
	
	
	
	

}
