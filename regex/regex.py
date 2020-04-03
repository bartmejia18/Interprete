import re

#Definir Inicio y Final
regexInicio = "PROCESO ([a-z][a-zA-Z0-9]*)"
regexFin = "FINPROCESO"

#Definir variables
regexDefinir = "DEFINIR ([a-z][a-z0-9A-Z_]*) COMO (ENTERO|REAL|LOGICO|TEXTO);"

#Definir asignaciones a variables
regexSet = re.compile(r'([a-z][a-zA-Z0-9_]*)<-([0-9.]+|".*"|Falso|Verdadero|[a-zA-Z0-9._]+);')

#Definir operaciones (+ - * /)
regexOperacion1 = '([a-z][a-zA-Z0-9_]*)<-(([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*)\s?((\+|\-|\*|\/)\s?([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*);)$)'

#Definir operaciones (sqrt, square, cube, cubert)
regexOperacion2 = '([a-z][a-zA-Z0-9_]*)<-((sqrt|square|cube|cubert)\s([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*))$'

#Verificar tipo de dato 
regexString = re.compile(r'^"[a-zA-Z0-9]+')
regexFloat = re.compile(r'[0-9]+\.')
regexInt = re.compile(r'[0-9]+')
regexBoolean = re.compile(r'(True|False)')

#Sentencia LEER
regexLeer = 'LEER ([a-zA-Z0-9_.]+);'

#Sentencia ESCRIBIR
regexEscribir = 'ESCRIBIR (".*");'

#Sentencia ESCRIBIR_LINEA
regexEscribirLinea = re.compile(r'ESCRIBIR_LINEA\s(".*")(\s?\+\s?([a-zA-Z][a-zA-Z0-9_.]*))?;')