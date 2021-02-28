package com.company;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
		Date date = new Date();

    String Dato1,Dato2,Direccion,Telefono,DNI,Nacionalidad,npassword;
	String Usuario = "Sergio";
	String Password = "Password";
	int Intentos = 0;
	int Option,Pedido;
	boolean prueba = true;
	boolean estado = true;
	boolean proceso = true;
	do {
		if (Intentos < 3) {
		System.out.println("Ingrese el nombre del usuario:");
		Dato1 = sc.nextLine();
		System.out.println("Ingrese la contraseña:");
		Dato2 = sc.nextLine();
		Intentos++;

		if (Dato1.equals(Usuario) && Dato2.equals(Password)) {
			estado = false;
			System.out.println("\n\nBienvenido " + Dato1);
			while (prueba) {
				System.out.println("\nEscoja uno de las siguientes opciones\n" +
						"1. Cambiar la contraseña\n" +
						"2. Llenar la información de su perfil (Dirección, número de teléfono, DNI, Nacionalidad)\n" +
						"3. Pedido: Seleccione un (1) artículo el cual será enviado a su domicilio\n" +
						"4. Salir");
				Option = sc.nextInt();

				switch (Option) {

					case 1:
						System.out.println(" ");
						System.out.println("Ingrese la nueva contraseña:");
						npassword = sc.next();
						Password = npassword;
						System.out.println("La contraseña se a cambiado exitosamente.");
						break;


					case 2:
						System.out.println(" ");
						System.out.println("Ingrese su dirección:");
						Direccion = sc.nextLine();
						System.out.println("Ingrese su número de telefono:");
						Telefono = sc.nextLine();
						System.out.println("Ingrese su DNI:");
						DNI = sc.nextLine();
						System.out.println("Ingrese su nacionalidad:");
						Nacionalidad = sc.nextLine();

						System.out.println("Los datos ingresados fueron:\n\n" +
								"Direccion:  " + Direccion + "\n" +
								"Número de telefono  :" + Telefono + "\n" +
								"DNI  :" + DNI + "\n" +
								"Nacionalidad  :" + Nacionalidad);
						break;
					case 3:
						while (proceso) {
							System.out.println("Escoja uno de las siguentes opciones\n" +
									"1. Arroz con Puerco\n" +
									"2. Pizza con piña\n" +
									"3. Sopa de pollo");
							Pedido = sc.nextInt();
							if (Pedido == 1) {
								System.out.println("Su pedido esta en proceso, porfavor espere.\n" +
										"El cliente solicito una orden de Arroz con Puerco.");
								proceso = false;
							} else if (Pedido == 2) {
								System.out.println("Su pedido esta en proceso, porfavor espere.\n" +
										"El cliente solicito una orden de Pizza de melon.");
								proceso = false;
							} else if (Pedido == 3) {
								System.out.println("Su pedido esta en proceso, porfavor espere.\n" +
										"El cliente solicito una orden de Sopa de pollo.");
								proceso = false;
							} else {
								System.out.println("Escriba solo el numero de la orden que quiere solicitar\n");
							}
						}
						break;
					case 4:
						System.out.println("Su orden fue completada con éxito, a la hora " + dateFormat.format(date) + " - La misma será enviada a su domicilio");
						prueba = false;
						break;
					default:
						throw new IllegalStateException("Unexpected value: " + Option);
				}
			}
		} else {
			System.out.println("El  nombre o la contraseña que ingresaste no coinciden con ninguna cuenta.\nIntentelo denuevo.\n");
		}
	}else {
			System.out.println("El Usuario a sobrepasado el limites de 3 intentos y se bloqueara el acceso durante 1 hora.");
			estado = false;
		}
	}while (estado);
    }
}
