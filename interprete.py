import re
import regex.regex as rg
import os

diccionarioVariables = {}
diccionarioEscritura = {}
dicInstrucSinPuntoComa = {}
cantTabs = 0

def tipoValor(valor):
    if re.match(rg.regexString, valor):
        return "TEXTO"
    if re.match(rg.regexFloat, valor):
        return "REAL"
    if re.match(rg.regexInt, valor):
        return "ENTERO"
    if re.match(rg.regexBoolean, valor):
        return "LOGICO"

def eliminarTabs():
    global cantTabs
    cantTabs = cantTabs - 1

def escribirArchivo(tab, linea):
    global cantTabs
    if tab == 0:
        tabs = '\t' * cantTabs
        archivoSalida.writelines(tabs+linea)
    else:
        cantTabs = cantTabs + tab
        tabs = '\t' * (cantTabs - 1)
        archivoSalida.writelines(tabs+linea)
        

def asignacionOperacion(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    valorVariable = codigo[1]
    if nombreVariable in diccionarioVariables:
        escribirArchivo(0,nombreVariable + " = " + valorVariable + '\n')

def asignacionValor(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    valorVariable = codigo[1]
    if nombreVariable in diccionarioVariables:
        tipoAsignacion = tipoValor(valorVariable)
        if diccionarioVariables[nombreVariable] == tipoAsignacion:
            if(valorVariable == "Verdadero"):
                valorVariable = "True"
            elif(valorVariable == "Falso"):
                valorVariable = "False"
            escribirArchivo(0,nombreVariable + " = " + valorVariable + '\n')
        else:
            print("Error: 0x02 - Inconsistencia de datos, se esperaba "+ diccionarioVariables[nombreVariable] +" y se encontró "+ tipoAsignacion +".")
    else:
        print("Error: 0x01 - '" + nombreVariable +"' instruccion o variable no definida")

def definirVariable(codigo):
    codigo = codigo[0]
    nombreVariable = codigo[0]
    tipoVariable = codigo[1]
    diccionarioVariables[nombreVariable] = tipoVariable

def definirLeer(codigo):
    variable = codigo[0]
    if variable in diccionarioVariables:
        diccionarioEscritura[variable] = diccionarioEscritura.pop('temp')
        escribirArchivo(0,variable + ' = input(' + diccionarioEscritura[variable] + ')\n' )
    else:
        print("Error: 0x01 - '" + variable +"' instruccion o variable no definida")

def definirEscribir(codigo):
    diccionarioEscritura['temp'] = codigo[0]

def definirEscribirLinea(codigo):    
    stringEscribirLinea = ""
    for item in codigo:
        if (re.match(rg.regexVarible, item)):
            if (item in diccionarioVariables):
                stringEscribirLinea = stringEscribirLinea + item
            else: 
                print("Error: 0x01 - '" + item +"' instruccion o variable no definida")
        elif (re.match(rg.regexValor, item)):
            stringEscribirLinea = stringEscribirLinea + ' ' + item
        elif (re.match(rg.regexConvertirTexto, item)):
            variable = item.split("(")[1].split(")")[0]
            if (variable in diccionarioVariables):
                stringEscribirLinea = stringEscribirLinea + 'str('+variable+')'
            else: 
                print("Error: 0x01 - '" + item +"' instruccion o variable no definida")
        elif ( "+" in item ):
            stringEscribirLinea = stringEscribirLinea + "+"

    escribirArchivo(0,'print('+stringEscribirLinea+')\n')

def inicioProceso(codigo):
    global diccionarioFuncion
    diccionarioFuncion = codigo
    escribirArchivo(1,'def '+codigo+'():\n')

def finProceso():
    escribirArchivo(-1,diccionarioFuncion+"()")

def definirSi(codigo):
    stringSi = "("
    count = 0
    for item in codigo:
        count = count + 1
        if (re.match(rg.regexVarible, item)):
            if (item in diccionarioVariables):
                stringSi = stringSi + item
            else: 
                print("Error: 0x01 - '" + item +"' instruccion o variable no definida")
        elif (re.match(rg.regexComparacion, item)):
            stringSi = stringSi + ' ' + item
        elif (re.match(rg.regexLogico, item)):
            count = 0
            operadorLogico = ""
            if (item == 'Y'):
                operadorLogico = 'and'
            else:
                operadorLogico = 'or'
            stringSi = stringSi + ' ' + operadorLogico + ' ('
        elif (re.match(rg.regexValor, item)):
            stringSi = stringSi + ' ' + item
        
        if (count == 3):
            stringSi = stringSi + ")"
    
    escribirArchivo(1,"if "+stringSi+":\n")

def definirSiNo():
    eliminarTabs()
    escribirArchivo(1,'else:\n')

def definirFinSi():
    eliminarTabs()

def definirMientras(codigo):
    stringMientras = "("
    for item in codigo:
        if (re.match(rg.regexVarible, item)):
            if (item in diccionarioVariables):
                stringMientras = stringMientras + item
            else: 
                print("Error: 0x01 - '" + item +"' instruccion o variable no definida")
        elif (re.match(rg.regexComparacion, item)):
                stringMientras = stringMientras + ' ' + item
        elif (re.match(rg.regexValor, item)):
            stringMientras = stringMientras + ' ' + item
    stringMientras = stringMientras + ")"
    escribirArchivo(1, "while "+stringMientras+":\n")

def definirFinMientras():
    eliminarTabs()

def intepretarArchivo(nombre):
    print("Interpretando ....")
    print("\b")
    file = open(nombre, "r")
    os.system('python ' + file.name)

def compilador(nombreArchivo, ejecutar):
    
    print("Traduciendo ....")

    if os.path.isfile(nombreArchivo):
        
        nombreArchivo = nombreArchivo.split(".")
        global archivoSalida 
        archivoSalida = open(nombreArchivo[0]+".py", "w")
        archivoEntrada = open(nombreArchivo[0]+".X", "r")

        for linea in archivoEntrada.readlines():
            if re.search(rg.regexInicio, linea):
                codigo = re.findall(rg.regexInicio, linea)                        
                inicioProceso(codigo[0])

            if re.search(rg.regexFin, linea):
                finProceso()                    
                
            if re.search(rg.regexDefinir, linea):
                codigo = re.findall(rg.regexDefinir, linea)                        
                definirVariable(codigo)
            
            if re.search(rg.regexOperacion1, linea):
                codigo = re.findall(rg.regexOperacion1, linea)
                asignacionOperacion(codigo)
            elif re.search(rg.regexOperacion2, linea):
                codigo = re.findall(rg.regexOperacion2, linea)
                asignacionOperacion(codigo)
            elif re.search(rg.regexSet, linea):
                codigo = re.findall(rg.regexSet, linea)
                asignacionValor(codigo)
            elif re.search(rg.regexEscribir, linea):
                codigo = re.findall(rg.regexEscribir, linea)
                definirEscribir(codigo)
            elif re.search(rg.regexLeer, linea):
                codigo = re.findall(rg.regexLeer, linea)
                definirLeer(codigo)
            elif re.search(rg.regexEscribirLinea, linea):
                codigo = re.findall(rg.regexEscribirLinea, linea)
                definirEscribirLinea(codigo[0])
            elif re.search(rg.regexSi, linea):
                codigo = re.findall(rg.regexSi, linea)
                definirSi(codigo[0])
            elif re.search(rg.regexSiNo, linea):
                codigo = re.findall(rg.regexSiNo, linea)
                definirSiNo()
            elif re.search(rg.regexFinSi, linea):
                codigo = re.findall(rg.regexFinSi, linea)
                definirFinSi()
            elif re.search(rg.regexMientras, linea):
                codigo = re.findall(rg.regexMientras, linea)
                definirMientras(codigo[0])
            elif re.search(rg.regexFinMientras, linea):
                codigo = re.findall(rg.regexFinMientras, linea)
                definirFinMientras()

        archivoSalida.close()
        archivoEntrada.close()
        print("Archivo generado: " + archivoSalida.name)
        if ejecutar == True:
            intepretarArchivo(archivoSalida.name)
    else:
        print("Error! Archivo no existe")

    