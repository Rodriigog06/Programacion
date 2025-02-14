package EjPersonaYEntrenador;

public class Entrenador {
	private String idFederacion;

	protected Entrenador(String idFederacion) {
		super();
		this.idFederacion = idFederacion;
	}

	protected String getIdFederacion() {
		return idFederacion;
	}

	protected void setIdFederacion(String idFederacion) {
		this.idFederacion = idFederacion;
	}
	
	

}
