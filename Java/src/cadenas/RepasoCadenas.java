package cadenas;

public class RepasoCadenas {
	public static void main(String[] args) {
		String cadena = "Hello planet earth, a great planet.";
		String cadena2= cadena.replaceAll("et", "ET");
		String cadena3= cadena.replace("et", "ET");
		System.out.println(cadena);
		System.out.println(cadena2);
		System.out.println(cadena3);
		
	}
	int suma(int x, int y)
	{
		return x+y;
	}
}
