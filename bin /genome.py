import os

"""
Este módulo contiene funciones para cargar un genoma desde un archivo FASTA.
"""

def cargar_genoma(path_genoma):
    """Carga el genoma desde un archivo FASTA (ignora la línea del encabezado '>') y devuelve el genoma"""
    
    secuencia = []
    if not os.path.isfile(path_genoma): #Validacion de existencia del archivo
        raise FileNotFoundError(f"El archivo de genoma no se encontró: {path_genoma}")
    
    with open(path_genoma, "r") as archivo:
        for linea in archivo:
            if not linea.startswith(">"):
                secuencia.append(linea.strip())

    return "".join(secuencia) #Sola cadena de texto con la secuencia del genoma 
