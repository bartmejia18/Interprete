import re
import regex.regex as rg

nombreArchivo = "prueba1"
archivoSalida = open(nombreArchivo+".py", "w")

diccionarioVariables = {}

def tipoValor(valor):
    if re.match(rg.regexString, valor):
        return "TEXTO"
    if re.match(rg.regexFloat, valor):
        return "REAL"
    if re.match(rg.regexInt, valor):
        return "ENTERO"
    if re.match(rg.regexBoolean, valor):
        return "LOGICO"

def asignacionOperacion(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    valorVariable = codigo[1]
    if nombreVariable in diccionarioVariables:
        archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')

def main():

    archivo = open(nombreArchivo+".X", "r")

    for linea in archivo.readlines():
        if(bool(re.match(rg.regexDefinir, linea)) == True):
            codigo = re.findall(rg.regexDefinir, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            tipoVariable = codigo[1]
            diccionarioVariables[nombreVariable] = tipoVariable
            if(tipoVariable == "ENTERO"):
                valorVariable = "0"
            elif(tipoVariable == "TEXTO"):
                valorVariable = '""'
            elif(tipoVariable == "LOGICO"):
                valorVariable = "False"
            elif(tipoVariable == "REAL"):
                valorVariable = "0.0"
            archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')      
        # else:
        #     print("Error, el tipo de dato no se reconoce.")
        #     break;

        if re.match(rg.regexOperacion1, linea):
            codigo = re.findall(rg.regexOperacion1, linea)
            asignacionOperacion(codigo)
        elif re.match(rg.regexOperacion2, linea):
            codigo = re.findall(rg.regexOperacion2, linea)
            asignacionOperacion(codigo)
        elif(re.match(rg.regexSet, linea)):
            codigo = re.findall(rg.regexSet, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            valorVariable = codigo[1]
            if nombreVariable in diccionarioVariables:
                if diccionarioVariables[nombreVariable] == tipoValor(valorVariable):
                    if(valorVariable == "Verdadero"):
                        valorVariable = "True"
                    elif(valorVariable == "Falso"):
                        valorVariable = "False"
                    archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')
                else:
                    print('Error: Asignacicion incorrecta')
            else:
                print('Error: Variable desconocida')

main()