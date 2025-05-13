import os

def extraer_secuencias(peaks, genoma):
    """
    Extrae fragmentos de la secuencia del genoma según coordenadas de picos.
    Retorna un diccionario agrupado por TF_name.
    """
    secuencia_TF = {}
    for pico in peaks:
        TF = pico["TF_name"]
        inicio = pico["start"]
        fin = pico["end"]
        secuencia = genoma[inicio:fin]

        if TF not in secuencia_TF:
            secuencia_TF[TF] = []
        secuencia_TF[TF].append(secuencia)
    
    return secuencia_TF


def guardar_fasta_por_tf(secuencia_TF, output):
    """
    Guarda archivos FASTA por cada TF con sus secuencias correspondientes.
    """
    if not os.path.exists(output):
        os.makedirs(output)

    for TF, secuencias in secuencia_TF.items():
        archivo_fasta = os.path.join(output, TF + ".fa")
        with open(archivo_fasta, "w") as archivo:
            for i, secuencia in enumerate(secuencias):
                archivo.write(f">peak_{i+1}\n{secuencia}\n")
