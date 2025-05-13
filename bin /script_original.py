"""
01/05/2025
Dulce Alejandra Carrillo Carlos 

Este script extrae secuencias de un genoma basado en las coordenadas 
de picos de unión de factores de transcripción y guarda cada 
secuencia en un archivo FASTA separado.

El script realiza lo siguiente:

1. Carga el genoma desde un archivo FASTA.
2. Lee un archivo de picos (.tsv) y extrae las coordenadas de inicio y fin de cada pico,
guiandose por las columnas que comprende el archivo. 
3. Extrae las secuencias del genoma utilizando las coordenadas de los picos.
4. Agrupa las secuencias por el nombre de cada TF.
5. Guarda las secuencias en archivos FASTA separados por cada TF.
6. Pide al usuario las rutas de los archivos de entrada y salida.

"""

import os #Para interactuar con el sistema operativo

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


def leer_archivo_picos(path_peaks):
    """Lee el archivo de picos (.tsv) e identifica las columnas de TF_name, Peak_start y Peak_end."""
    
    picos = []
    if not os.path.isfile(path_peaks): #Validacion de existencia del archivo
        raise FileNotFoundError(f"El archivo de picos no se encontró: {path_peaks}")

    with open(path_peaks, "r") as archivo:
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


def extraer_secuencias(peaks, genoma):
    """Usa las coordenadas para extraer fragmentos de genoma por cada TF."""

    secuencia_TF = {}
    for pico in peaks:
        TF = pico["TF_name"]
        inicio = pico["start"]
        fin = pico["end"]

        #Extraer la secuencia del genoma segun las coordenadas 
        secuencia = genoma[inicio:fin]
        
        if TF not in secuencia_TF:
            secuencia_TF[TF] = []
        secuencia_TF[TF].append(secuencia)

    return secuencia_TF


def guardar_fasta_por_tf(secuencia_TF, output):
    """Crea un archivo .fa por cada TF_name con las secuencias correspondientes."""

    if not os.path.exists(output):
        os.makedirs(output)

    for TF, secuencias in secuencia_TF.items():
        archivo_fasta = os.path.join(output, TF + ".fa")
        with open(archivo_fasta, "w") as archivo:
            for i, secuencia in enumerate(secuencias):
                archivo.write(f">peak_{i+1}\n{secuencia}\n")


#Solicitar al usuario las rutas de los archivos
#archivo_genoma= input("Ingrese la ruta del archivo de genoma (FASTA): ")
#archivo_picos= input("Ingrese la ruta del archivo de picos: ")
#carpeta_salida= input("Ingrese la ruta de la carpeta de salida: ")

#Ejemplo:
archivo_genoma = "/home/carrillo/Downloads/mk-fasta-meme/mk-fasta-meme/E_coli_K12_MG1655_U00096.3.txt"
archivo_picos = "/home/carrillo/Downloads/mk-fasta-meme/mk-fasta-meme/union_peaks_file.tsv"
carpeta_salida = "/home/carrillo/Downloads/mk-fasta-meme/resultados"

#MAIN
genoma = cargar_genoma(archivo_genoma)
picos = leer_archivo_picos(archivo_picos)
print("\nSe encontraron", len(picos), "picos.")
secuencias = extraer_secuencias(picos, genoma)
print("Se agruparon secuencias para", len(secuencias), "factores de transcripción únicos.")
print(f"Archivos FASTA por TF en la carpeta:{carpeta_salida}\n")
guardar_fasta_por_tf(secuencias, carpeta_salida)