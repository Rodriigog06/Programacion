package OrientacionAObjetos;

public class Edificios {
	int numPlantas = 0;
	float extension;
	String direccion;
	
	
	public Edificio() {	
		super();
		numPlantas =0;
		extension =100F;
		direccion = "Calle Pepe";
	}
	
	
	public Edificio(int numPlantas, float extension, String direccion) {
		super ();
		this.numPlantas = numPlantas;
		this.extension = extension;
		this.direccion = direccion;
	}
}
  