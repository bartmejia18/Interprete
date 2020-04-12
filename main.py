import interprete

def main():
    ejecutar = True
    while ejecutar:
        comando = input("#>> ")
        instruccion = comando.split()
        if 'compile' in comando: 
            interprete.compilador(instruccion[1], False)
        elif 'run' in comando:
            interprete.compilador(instruccion[1], True)
        elif 'load' in comando:
            interprete.intepretarArchivo(instruccion[1])
        elif comando == "exit":
            print('Saliendo ....')
            ejecutar = False
            
main()

