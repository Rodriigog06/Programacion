package cadenas;

public class folio2 {

	public static void main(String[] args) {

		    folio2 r = new folio2();
		    String [] palabras = r.cargatabla();
		    System.out.println(palabras);
		    r.imprimeTabla (palabras);
		    r.filtraNumeros (palabras);
		    System.out.println("Termino");
		    }
		    String [] cargatabla() {
		        System.out.println("Introduce tu frase: ");
		        Scanner sc = new Scanner (System.in);
		        String frase = sc.nextLine();
		        String[] tabla = frase.split(" ");
		        return tabla;
		        }
		    void imprimeTabla (String [] tabla) {
		        for (String elemento:tabla)
		        {
		            System.out.println(elemento);
		        }
		    }
		    String[] filtraNumeros (String[] tabla) {
		    {
		        String[] numeros = new String [tabla.length];
		        for (int i= 0; i < tabla.length;i++);
		        {

		            if(isCadenaEsNumero(tabla[i]))
		            {
		                numeros[i] = tabla[i];
		            }
		        }
		        return numeros;
		    
		    }
		    boolean isCadenaEsNumero(String palabra)
		    {
		        boolean es = false;
		        for(int i = 0; i < palabra.length(); i++)
		        {
		        return es;
		        }
		    }
		    }
		    
		    }
		}

	}

}
