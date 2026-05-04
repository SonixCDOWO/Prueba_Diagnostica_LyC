def verificar_collatz():
    print("--- VERIFICADOR DE LA CONJETURA DE COLLATZ ---")
    try:
        # convertimos las entradas de texto a numeros enteros
        p = int(input("Ingrese el limite inferior (p): "))
        q = int(input("Ingrese el limite superior (q): "))

        # verificamos la regla de negocio que pide el problema
        if q < 100 * p:
            print(f"\nERROR: q ({q}) debe ser al menos 100 veces p ({100*p}).")
        else:
            print(f"\nProcesando intervalo [{p}, {q}]...\n")
            # recorremos cada numero en el rango desde p hasta q
            for n_actual in range(p, q + 1):
                n = n_actual
                camino = [str(n)] # lista para guardar la secuencia de numeros
                
                # el ciclo sigue hasta que el numero llegue a 1
                while n != 1:
                    if n % 2 == 0: 
                        n //= 2 # si es par, se divide entre dos
                    else: 
                        n = 3 * n + 1 # si es impar, 3n + 1
                    camino.append(str(n)) # agregamos el nuevo numero a la lista
                
                # imprimimos la secuencia usando una flecha como separador
                print(f"n={n_actual}: {' -> '.join(camino)}")
            
            print("\nConjetura demostrada en el rango.")
            
    except ValueError:
        # si el usuario mete letras en vez de numeros, captura el error
        print("\nError: Debe ingresar numeros enteros.")

    print("===========================================")
    # pausa para que el usuario pueda leer todas las secuencias
    input("\nPresione ENTER para salir...")

if __name__ == "__main__":
    verificar_collatz()
