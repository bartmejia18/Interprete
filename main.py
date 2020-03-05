import re
regexDefinir = "DEFINIR ([a-z][a-z0-9A-Z_]*) COMO (ENTERO|REAL|LOGICO|TEXTO);"
regexSet = '([a-z][a-zA-Z0-9_]*)<-([0-9.]+|".*"|Falso|Verdadero|([a-zA-Z0-9_.]*\s?(\+|\*|\-|\/)\s?[a-zA-Z0-9_.]+)|[a-zA-Z]*);'

def main():
    nombreArchivo = "prueba1"
    archivo = open(nombreArchivo+".X", "r")
    archivoSalida = open(nombreArchivo+".py", "w")
    for linea in archivo.readlines():
        if(bool(re.search(regexDefinir, linea)) == True):
            codigo = re.findall(regexDefinir, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            tipoVariable = codigo[1]
            if(tipoVariable == "ENTERO"):
                valorVariable = "0"
            elif(tipoVariable == "TEXTO"):
                valorVariable = '""'
            elif(tipoVariable == "LOGICO"):
                valorVariable = "False"
            elif(tipoVariable == "REAL"):
                valorVariable = "0.0"
            else:
                print("Error, el tipo de dato no se reconoce.")
            archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')
            print(linea + " -> " + nombreVariable + " = " + valorVariable)
        elif((bool(re.search(regexSet, linea)) == True)):
            codigo = re.findall(regexSet, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            valorVariable = codigo[1]
            if(valorVariable == "Verdadero"):
                valorVariable = "True"
            elif(valorVariable == "Falso"):
                valorVariable = "False"
            archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')
            print(linea + " -> " + nombreVariable + " = " + valorVariable)
main()