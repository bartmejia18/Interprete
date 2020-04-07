PROCESO principal
    DEFINIR numero COMO ENTERO;
    DEFINIR contador COMO ENTERO;
    ESCRIBIR "Ingrese numero: ";
    LEER numero;
    contador<-0;
    contador<-square numero;
    ESCRIBIR_LINEA contador;
    MIENTRAS (contador != numero) HACER
        contador<-contador+1;
        ESCRIBIR_LINEA "contador:" + contador;
    FINMIENTRAS
FINPROCESO