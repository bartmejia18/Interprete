import re
import regex.regex as rg

nombreArchivo = "prueba1"
archivoSalida = open(nombreArchivo+".py", "w")

diccionarioVariables = {}
diccionarioEscritura = {}

def tipoValor(valor):
    if re.match(rg.regexString, valor):
        return "TEXTO"
    if re.match(rg.regexFloat, valor):
        return "REAL"
    if re.match(rg.regexInt, valor):
        return "ENTERO"
    if re.match(rg.regexBoolean, valor):
        return "LOGICO"

def escribirArchivo(linea):
    archivoSalida.writelines(linea)

def asignacionOperacion(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    valorVariable = codigo[1]
    if nombreVariable in diccionarioVariables:
        escribirArchivo(nombreVariable + " = " + valorVariable + '\n')

def asignacionValor(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    valorVariable = codigo[1]
    if nombreVariable in diccionarioVariables:
        if diccionarioVariables[nombreVariable] == tipoValor(valorVariable):
            if(valorVariable == "Verdadero"):
                valorVariable = "True"
            elif(valorVariable == "Falso"):
                valorVariable = "False"
            escribirArchivo(nombreVariable + " = " + valorVariable + '\n')
        else:
            print('Error: Asignacicion incorrecta')
    else:
        print('Error: Variable desconocida')

def definirVariable(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    tipoVariable = codigo[1]
    diccionarioVariables[nombreVariable] = tipoVariable

def definirLeer(codigo):
    variable = codigo[0]
    if variable in diccionarioVariables:
        diccionarioEscritura[variable] = diccionarioEscritura.pop('temp')
        escribirArchivo(variable + ' = raw_input(' + diccionarioEscritura[variable] + ')\n' )
    else:
        print("Error: No se encontro la variable")

def definirEscribir(codigo):
    diccionarioEscritura['temp'] = codigo[0]

def definirEscribirLinea(codigo):    
    if codigo[2] == '':
        escribirArchivo('print('+codigo[0]+')')
    else:
        if codigo[2] in diccionarioVariables:
            escribirArchivo('print('+codigo[0]+' + '+codigo[2]+')\n')
        else:
            print("Error: No se encontro la variable")

def inicioProceso(codigo):
    global diccionarioFuncion
    diccionarioFuncion = codigo
    escribirArchivo('def '+codigo+'():\n')

def finProceso():
    escribirArchivo(diccionarioFuncion+"()")

def main():

    archivo = open(nombreArchivo+".X", "r")

    for linea in archivo.readlines():
        if re.match(rg.regexInicio, linea):
            codigo = re.findall(rg.regexInicio, linea)                        
            inicioProceso(codigo[0])

        if re.match(rg.regexFin, linea):
            finProceso()                    
            

        if re.match(rg.regexDefinir, linea):
            codigo = re.findall(rg.regexDefinir, linea)                        
            definirVariable(codigo)
        
        if re.match(rg.regexOperacion1, linea):
            codigo = re.findall(rg.regexOperacion1, linea)
            asignacionOperacion(codigo)
        elif re.match(rg.regexOperacion2, linea):
            codigo = re.findall(rg.regexOperacion2, linea)
            asignacionOperacion(codigo)
        elif re.match(rg.regexSet, linea):
            codigo = re.findall(rg.regexSet, linea)
            asignacionValor(codigo)

        elif re.match(rg.regexEscribir, linea):
            codigo = re.findall(rg.regexEscribir, linea)
            definirEscribir(codigo)

        elif re.match(rg.regexLeer, linea):
            codigo = re.findall(rg.regexLeer, linea)
            definirLeer(codigo)

        elif re.match(rg.regexEscribirLinea, linea):
            codigo = re.findall(rg.regexEscribirLinea, linea)
            definirEscribirLinea(codigo[0])
main()

