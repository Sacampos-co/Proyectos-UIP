package com.company;

import com.sun.management.UnixOperatingSystemMXBean;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner scan = new Scanner(System.in);
        float inv=0, its=0, tot=0, itspag1=0, itspag2=0, itspag3=0;
        int cantcl=0, s;
        String nom, ape, cedu, opc="", totclin="", reporte = "\t\tCEDULA         MONTO DE INVERSIÓN     INTERÉS    TOTAL \n";
        while (!opc.equals("no"))
        {

            System.out.println("\t\tBANCO A B C");
            System.out.println("Numero de cedula del cliente separados por guiones : " );
            cedu=scan.nextLine();
            System.out.println("Nombre del cliente : ");
            nom=scan.nextLine();
            System.out.println("Apellido del cliente : ");
            ape=scan.nextLine();
            System.out.println("\t\tInversion del Cliente: ");
            inv=Float.parseFloat(scan.nextLine());

            if (inv<=500)
            {

                its = inv*0.015f;
                itspag1+= its;
                tot = its+inv;
            }
            else
            if (inv> 500 && inv<=1000)
            {
                its = inv*0.020f;
                itspag2+=its;
                tot = its+inv;
            }
            else if (inv>1000)
            {
                its = inv*0.025f;
                itspag3+=its;
                tot = its+inv;
            }
            System.out.println("\tCLIENTE: "+nom+"\t "+ape);
            System.out.println("\tCEDULA: "+cedu);
            System.out.println("\tMONTO DE INVERSIÓN : "+inv);
            System.out.println("\tINTERÉS GENERADO EN ESTE MES: "+its);
            System.out.println("\tTOTAL GENERADO EN ESTE MES: "+tot);
            System.out.println("\tCedula= "+cedu+"\tInversion= "+inv+"\tInteres= "+its+"\tTotal= "+tot+" ");
            System.out.println("\tCONTINUAR: SI o NO  ");

            cantcl++;
            totclin=totclin+" "+cantcl+"\t\t"+cedu+"\t\t"+inv+"\t\t\t\t"+its+"\t\t"+tot+"\n";
            opc=scan.nextLine();
        }

        System.out.println("\n\t\t\t\t\tBANCO A B ");
        System.out.println(reporte);
        System.out.println(totclin);
        System.out.println("\tTOTAL DE CLIENTES PROCESADOS: "+cantcl);
        System.out.println("\t\tTOTAL DE INTERESÉS PAGADOS AL 1.5%: "+itspag1);
        System.out.println("\t\tTOTAL DE INTERESÉS PAGADOS AL 2.0%: "+itspag2);
        System.out.println("\t\tTOTAL DE INTERESÉS PAGADOS AL 2.5%: "+itspag3);


    }
}
