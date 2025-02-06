package Simulacro;

import java.util.Scanner;

public class Simulacro2 {

	public static void main(String[] args) {
		
        Scanner input = new Scanner (System.in);
        Ejercicio1 f = new Ejercicio1();
        String respuestaUsuario = "";
        String nombreAutor = "";
        char Sexo;
        String tituloLibro = "";
        double PrecioLibro = 0;
        int unidadesVendidas = 0;
        
        String opcion = f.menu(input);
        
        while (!opcion.equals("S")) {
            System.out.println("\\n == Menú ==");
            System.out.println("R. Registrar libros.");
            System.out.println("%. Mostrar el porcentaje del sexo del autor.");
            System.out.println("P. Mostrar el precio del libro (caro y barato)");
            System.out.println("V. Mostrar el libro que más se ha vendido.");
            System.out.println("S. Salir");
            System.out.println("Seleccione una de estas opciones: ");
            opcion = input.nextLine().toUpperCase();
            
            switch (opcion) {
            case "R":
                //registroDeLibros ();
                break;
            case "%":
                //porcentajesexo ();
                break;
            case "P":
                //baratoycaro ();
                break;
            case "V":
                //libroMasVendido ();
                break;
            case "S":
                System.out.println("El programa ha finalizado con exito.");
                break;
            default:
                System.out.println("La opcion que has seleccionado no es válida. Intentalo de nuevo.");
            }
        }
    }
    
    String menu(Scanner input){
        System.out.println("R - Registrar Libros");
        System.out.println("% - Mostrar % libros por sexo del autor");
        System.out.println("P - Mostrar libro más barato y más caro");
        System.out.println("V - Mostrar libro más vendido");
        System.out.println("S - Salir.");

        String respuestaUsuario = input.next();
        respuestaUsuario = respuestaUsuario.toUpperCase();
        return respuestaUsuario;
		            }
		        
		    
		

	}


