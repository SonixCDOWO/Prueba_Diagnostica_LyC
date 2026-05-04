#1) Dado una cadena de expresión aritmética imprima cada componente 
#según su clasificación
#( NUMERO, OPERADOR, PAREN_IZQ, PAREN_DER, OPERANDO, ERROR).

#Reglas:
#NUMERO: debe ser un entero o un real con el “.”, como marcador de 
#decimales, sin signo
#OPERANDO: no debe tener espacios ni iniciar con un numero (VALOR, 
#A, B, CONT)
#OPERADOR: + - * /

import re # importamos la libreria de expresiones regulares

def analizar_expresion():
    print("--- ANALIZADOR LÉXICO DE EXPRESIONES ---")
    # pedimos al usuario que escriba la cadena por teclado
    cadena = input("Ingrese la expresion a analizar: ")

    # definimos los patrones de los tokens usando expresiones regulares
    # cada tupla tiene el nombre del token y su regla matemática
    patrones = [
        ('NUMERO', r'\d+(\.\d+)?'),       # numeros enteros o con punto decimal
        ('OPERADOR', r'[\+\-\*/]'),       # busca los signos +, -, *, /
        ('PAREN_IZQ', r'\('),             # busca el paréntesis que abre
        ('PAREN_DER', r'\)'),             # busca el paréntesis que cierra
        ('OPERANDO', r'[a-zA-Z][a-zA-Z0-9]*'), # letras que no empiezan con número
        ('ESPACIO', r'\s+'),              # detecta espacios en blanco para ignorarlos
    ]

    # unimos todos los patrones en una sola cadena de busqueda
    regex_combinada = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones)
    
    tokens_encontrados = [] # lista para guardar los resultados
    pila_parentesis = 0     # contador para ver si los parentesis estan bien cerrados
    error_balance = False   # bandera para marcar si hay un error de cierre

    # buscamos todos los tokens en la cadena ingresada
    for mo in re.finditer(regex_combinada, cadena):
        tipo = mo.lastgroup  # obtenemos el nombre del token (ej. NUMERO)
        valor = mo.group(tipo) # obtenemos el texto real (ej. 12.5)

        if tipo == 'ESPACIO': continue # si es un espacio, no hacemos nada
        
        # lógica para balancear parentesis
        if tipo == 'PAREN_IZQ': 
            pila_parentesis += 1 # sumamos si abre
        elif tipo == 'PAREN_DER': 
            pila_parentesis -= 1 # restamos si cierra
        
        # si el contador es negativo, cerraron un parentesis antes de abrirlo
        if pila_parentesis < 0: error_balance = True
            
        # guardamos el nombre del token y su valor en la lista
        tokens_encontrados.append(f"{tipo} {valor}")

    # verificamos si al final el contador quedo en cero
    if pila_parentesis == 0 and not error_balance:
        resultado_balance = "PARÉNTESIS BALANCEADOS"
    else:
        resultado_balance = "ERROR EN PARÉNTESIS"

    # mostramos el resultado final por pantalla
    print("\n================ RESULTADO ================")
    print(" ".join(tokens_encontrados) + ". " + resultado_balance)
    print("===========================================")
    
    # pausa para que no se cierre la ventana de comandos
    input("\nPresione ENTER para salir...")

if __name__ == "__main__":
    analizar_expresion()
