package Pokemon;

public class Ejercicio {

	public static void main(String[] args) {
	
		Pokemon pikachu = new Pokemon();
		pikachu.nombre = "Pikachu";
		pikachu.nivel = 12;
		pikachu.tipo = "Electrico";
		
		Pokemon mew2 = new Pokemon();
		mew2.nombre = "Mewto";
		mew2.nivel = 20;
		mew2.tipo = "Psiquico";
		
		String cadenaPikachu = pikachu.convierteEnCadena();
		System.out.println(cadenaPikachu);
		
		System.out.println("Pokemon 2 :" +mew2.nombre );
		
		System.out.println("Pokemon 1:"+pikachu.nombre + "Nivel" +pikachu.nivel + "Tipo" +pikachu.tipo);
		pikachu.nivel = pikachu.nivel+2;
		System.out.println("Pokemon 2:"+mew2.nombre + "Nivel" +mew2.nivel + "Tipo" +mew2.tipo);
		
		System.out.println("Pokemon 2:" +mew2.nombre);
	}

}
