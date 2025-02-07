package Boletin3;

public class CuentaBancaria {
	
	private double saldo;
	private String numCuenta;
	private Personas3 titular;
	private Personas3 autorizado;
	
	public CuentaBancaria(double saldo, String numCuenta, Personas3 titular) {
		super();
		this.saldo = saldo;
		this.numCuenta = numCuenta;
		this.titular = titular;
		this.autorizado = autorizado;
	}

	public double getSaldo() {
		return saldo;
	}

	void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public String getNumCuenta() {
		return numCuenta;
	}

	public void setNumCuenta(String numCuenta) {
		this.numCuenta = numCuenta;
	}

	public Personas3 getTitular() {
		return titular;
	}

	public void setTitular(Personas3 titular) {
		this.titular = titular;
	}

	public Personas3 getAutorizado() {
		return autorizado;
	}

	public void setAutorizado(Personas3 autorizado) {
		this.autorizado = autorizado;
	}
	
	private boolean validacionImportepositivo(double importe) {
		return importe >0;
	}
	
	private boolean validarAutorizado(String dni) {
		return dni != null && dni.equals(autorizado.getDni());
	}
	
	public void ingresarDinero(Personas3 autorizado, double ingreso) {
		if (validarAutorizado(autorizado.getDni()) && validacionImportepositivo(ingreso)) {
			setSaldo(getSaldo() + ingreso);
		} else {
			System.out.println("ERROR: No es autorizado o ingreso correcto");
		}
		
	}
	
	public void retiradaDinero(Personas3 personagestion, double reintegro) {
		if (validarAutorizado(personagestion.getDni()) && validacionImportepositivo(reintegro)
				&& (getSaldo() >= reintegro)) {
		} else {
		System.out.println("ERROR: No es autorizado o ingreso correcto o saldo insuficiente");
		}
	}
	
	public void eliminarAutorizado(String dni) {
		if (validarAutorizado(dni)) {
			autorizado = null;
			
		} else {
			System.out.println("ERROR: La persona introducida no es correcta");
		}
	}
}



















