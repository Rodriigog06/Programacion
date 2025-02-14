package EjercicioPresentacion;

public class Profesor extends Persona {
	
	protected String nombreDepartamentos;

	protected String getNombreDepartamentos() {
		return nombreDepartamentos;
	}

	protected void setNombreDepartamentos(String nombreDepartamentos) {
		this.nombreDepartamentos = nombreDepartamentos;
	}

	public Profesor(String nombre, String nombreDepartamentos) {
		super(nombre);
		this.nombreDepartamentos = nombreDepartamentos;
		
		
	}



}
