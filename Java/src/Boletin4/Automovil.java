package Boletin4;

public class Automovil extends Vehiculo {

	
	private CalificacionEco calificacionEcologica = CalificacionEco.ECO;
	
	private enum CalificacionEco{
		ECO, O, B, C;
	}

    public Automovil(String dueño, int numPuertas, int numRuedas, String calificacionEcologica) {
        super(dueño, numPuertas, numRuedas);
        setCalificacionEcologica(calificacionEcologica);
    }

    public CalificacionEco getCalificacionEcologica() {
        return calificacionEcologica;
    }

    public void setCalificacionEcologica(CalificacionEco calificacionEcologica) {
        if(calificacionEcologica == (CalificacionEco.ECO) || calificacionEcologica == (CalificacionEco.O)||
        		calificacionEcologica == (CalificacionEco.B) ||calificacionEcologica == (CalificacionEco.C))
        	
        	
        	this.calificacionEcologica = calificacionEcologica;
    }
}
