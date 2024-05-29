def es_gramatica(cadena):
    # Dividimos la cadena en dos partes: N y C
    partes = cadena.split('=')
    if len(partes) != 2:
        return False

    N, C = partes

    if len(N) != 1 or N != 'N':
        return False

    if C not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return False

    return True

cadenas = ["N=1", "N=5", "C=9", "N=2", "C=10", "N=NC", "N=CC"]

for cadena in cadenas:
    if es_gramatica(cadena):
        print(f"{cadena}: Es una gramática válida.")
    else:
        print(f"{cadena}: No es una gramática válida.")