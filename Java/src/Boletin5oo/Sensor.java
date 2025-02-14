package Boletin5oo;

import java.util.Objects;

public class Sensor {
	private double distancia;
	private double velocidad;
	
	protected Sensor(double distancia, double velocidad) {
		super();
		this.distancia = distancia;
		this.velocidad = velocidad;
	}

	protected double getDistancia() {
		return distancia;
	}

	protected void setDistancia(double distancia) {
		if (distancia >0)
		this.distancia = distancia;
	}

	protected double getVelocidad() {
		return velocidad;
	}

	protected void setVelocidad(double velocidad) {
		this.velocidad = velocidad;
	}

	@Override
	public String toString() {
		return "Sensor [distancia=" + distancia + ", velocidad=" + velocidad + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(distancia, velocidad);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Sensor other = (Sensor) obj;
		return Double.doubleToLongBits(distancia) == Double.doubleToLongBits(other.distancia)
				&& Double.doubleToLongBits(velocidad) == Double.doubleToLongBits(other.velocidad);
	}
	
	


}
