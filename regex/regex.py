import re
regexDefinir = "DEFINIR ([a-z][a-z0-9A-Z_]*) COMO (ENTERO|REAL|LOGICO|TEXTO);"
regexSet = re.compile(r'([a-z][a-zA-Z0-9_]*)<-([0-9.]+|".*"|Falso|Verdadero|[a-zA-Z0-9._]+)')
regexOperacion1 = '([a-z][a-zA-Z0-9_]*)<-(([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*)\s?((\+|\-|\*|\/)\s?([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*))$)'
regexOperacion2 = '([a-z][a-zA-Z0-9_]*)<-((sqrt|square|cube|cubert)\s([0-9.]+|[a-zA-Z][a-zA-Z0-9_.]*))$'

regexString = re.compile(r'^"[a-zA-Z0-9]+')
regexFloat = re.compile(r'[0-9]+\.')
regexInt = re.compile(r'[0-9]+')
regexBoolean = re.compile(r'(True|False)')
