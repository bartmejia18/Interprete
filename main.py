import re
import regex.regex as rg

diccionarioVariables = {}

def validarVariable(valor):
    if re.match(rg.regexString, valor):
        return "TEXTO"
    if re.match(rg.regexFloat, valor):
        return "REAL"
    if re.match(rg.regexInt, valor):
        return "ENTERO"
    if re.match(rg.regexBoolean, valor):
        return "LOGICO"

def existeVariable(nombre, valor):
    if nombre in diccionarioVariables:
        if (diccionarioVariables[nombre] == validarVariable(valor)):
            return True
        else:
            return False
    else: 
        print('Error: Variable desconocida')
        return False

def main():
    nombreArchivo = "prueba1"
    archivo = open(nombreArchivo+".X", "r")
    archivoSalida = open(nombreArchivo+".py", "w")

    for linea in archivo.readlines():
        if(bool(re.search(rg.regexDefinir, linea)) == True):
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

        if((bool(re.search(rg.regexSet, linea)) == True)):
            codigo = re.findall(rg.regexSet, linea)
            codigo = codigo[0]
            nombreVariable = codigo[0]
            valorVariable = codigo[1]
            if (existeVariable(nombreVariable, valorVariable)):
                if(valorVariable == "Verdadero"):
                    valorVariable = "True"
                elif(valorVariable == "Falso"):
                    valorVariable = "False"
                archivoSalida.writelines(nombreVariable + " = " + valorVariable + '\n')
            else:
                print("Error: Asignacion incorrecta")
                break;
            
main()