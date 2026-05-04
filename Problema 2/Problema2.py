#2) Dado una cadena C, valide si C se encuentra en notación FEN 
#(Forsyth-Edwards Notation), Forsyth–Edwards Notation. FEN (Wikipedia, 2025).

import re # importamos la libreria para usar expresiones regulares

def validar_notacion_fen():
    print("--- VALIDADOR DE NOTACIÓN FEN (AJEDREZ) ---")
    print("Ejemplo valido: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    # recibimos la cadena fen desde el teclado
    fen = input("\nIngrese la cadena FEN: ")

    # esta expresión regular valida los 6 campos de la notacion fen:
    # 1. el tablero (piezas y filas)
    # 2. el turno (w o b)
    # 3. derechos de enroque (KQkq)
    # 4. captura al paso (casilla o -)
    # 5. contador de medios movimientos
    # 6. numero de la jugada completa
    regex_fen = r'^([rnbqkpRNBQKP1-8]{1,8}/){7}[rnbqkpRNBQKP1-8]{1,8} [wb] (K?Q?k?q?|-) ([a-h][36]|-) \d+ \d+$'

    print("\n================ RESULTADO ================")
    # comparamos la entrada del usuario con la regla regex
    if re.match(regex_fen, fen):
        print("Notacion FEN Valida")
    else:
        print("Notacion FEN Invalida")
    print("===========================================")
    
    # pausa para ver el resultado antes de cerrar
    input("\nPresione ENTER para salir...")

if __name__ == "__main__":
    validar_notacion_fen()
