import os
"""
Este módulo contiene funciones para extraer secuencias de un genoma basado en picos de unión de factores de transcripción (TF).
Las funciones incluyen la extracción de secuencias específicas y la creación de archivos FASTA para cada TF.
"""

def extraer_secuencias(peaks, genoma):
    """Usa las coordenadas para extraer fragmentos de genoma por cada TF.
    
    Parámetros: 
    peaks: Lista de diccionarios con la informaciómn de los picos de unión ("TF_name", "start" y "end").
    genoma: Secuencia

    Devuelve un diccionario donde las claves son los nombres de los TF y los valores son listas de secuencias extraídas.
    """

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
    """Crea un archivo .fa por cada TF_name con las secuencias correspondientes.
    
    Parámetros:     
    secuencia_TF: diccionario donde las claves son los nombres de los TF y los valores son listas de secuencias extraídas.
    output: Ruta de la carpeta donde se guardarán los archivos FASTA.
    """

    if not os.path.exists(output):
        os.makedirs(output)

    for TF, secuencias in secuencia_TF.items():
        archivo_fasta = os.path.join(output, TF + ".fa")
        with open(archivo_fasta, "w") as archivo:
            for i, secuencia in enumerate(secuencias):
                archivo.write(f">peak_{i+1}\n{secuencia}\n")