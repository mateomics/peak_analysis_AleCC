import os
import argparse
from genome import cargar_genoma
from peaks import leer_archivo_picos
from io_utils import extraer_secuencias, guardar_fasta_por_tf
from arg import parsear_argumentos

"""

Este script principal coordina la carga del genoma, la lectura de picos y la extracción de secuencias.
Genera archivos FASTA para cada factor de transcripción.

"""

def main():
    
    args = parsear_argumentos()

    try:
        genoma = cargar_genoma(args.genoma)
        picos = leer_archivo_picos(args.picos)
    except Exception as e:
        print(f"[ERROR]: {e}")
        return

    if not genoma or not picos:
        print("[ERROR]: Genoma vacío o sin picos válidos.")
        return

    print(f"\ Se encontraron {len(picos)} picos.")
    secuencias = extraer_secuencias(picos, genoma)
    print(f"Se agruparon secuencias para {len(secuencias)} TF únicos.")
    
    guardar_fasta_por_tf(secuencias, args.salida)
    print(f" Archivos FASTA generados en la carpeta: {args.salida}\n")


if __name__ == "__main__":
    main()

