import os 

"""
Este módulo contiene funciones para leer picos de unión de factores de transcripción (TF).
"""


def leer_archivo_picos(peaks_archivo):
    """Lee el archivo de picos (.tsv) e identifica las columnas de TF_name, Peak_start y Peak_end."""
    
    picos = []
    if not os.path.isfile(peaks_archivo): #Validacion de existencia del archivo
        raise FileNotFoundError(f"El archivo de picos no se encontró: {peaks_archivo}")

    with open(peaks_archivo, "r") as archivo:
        next(archivo) 
        for linea in archivo:
            filas = linea.strip().split("\t")
            pico = {
                "TF_name": filas[2],
                "start": int(float(filas[3])), 
                "end": int(float(filas[4])) 
            }
            picos.append(pico)
    return picos

