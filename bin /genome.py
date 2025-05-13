import os

def cargar_genoma(path_genoma):
    """
    Carga el genoma desde un archivo FASTA.
    Ignora las líneas que comienzan con '>'.
    Devuelve la secuencia completa como una cadena.
    """
    secuencia = []
    if not os.path.isfile(path_genoma):
        raise FileNotFoundError(f"El archivo de genoma no se encontró: {path_genoma}")
    
    with open(path_genoma, "r") as archivo:
        for linea in archivo:
            if not linea.startswith(">"):
                secuencia.append(linea.strip())

    return "".join(secuencia)
