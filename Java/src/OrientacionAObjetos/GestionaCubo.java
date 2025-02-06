package OrientacionAObjetos;

public class GestionaCubo {

	public static void main(String[] args) {

		        Cubo cubo1 = new Cubo(4,0);
		        System.out.println(cubo1);
		        
		        System.out.println(cubo1.llenar(6));
		        System.out.println(cubo1);
		        cubo1.vaciar(4);
		        System.out.println(cubo1);
		        System.out.println(cubo1.vaciar(3));
		        System.out.println(cubo1);
		        cubo1.llenar(16);
		        System.out.println(cubo1);
		    }

		

	}


