import os
from genome import cargar_genoma
from peaks import leer_archivo_picos
from io_utils import extraer_secuencias, guardar_fasta_por_tf

"""
Este script principal coordina la carga del genoma, la lectura de picos y la extracción de secuencias.
Genera archivos FASTA para cada factor de transcripción.

"""

def main():
    
    # Rutas relativas dentro del repositorio
    archivo_genoma = os.path.join("data", "E_coli_K12_MG1655_U00096.3.txt")
    archivo_picos = os.path.join("data", "union_peaks_file.tsv")
    carpeta_salida = "output"

    genoma = cargar_genoma(archivo_genoma)
    picos = leer_archivo_picos(archivo_picos)
    print(f"\nSe encontraron {len(picos)} picos.")

    secuencias = extraer_secuencias(picos, genoma)
    print(f"Se agruparon secuencias para {len(secuencias)} factores de transcripción únicos.")

    guardar_fasta_por_tf(secuencias, carpeta_salida)
    print(f"Archivos FASTA generados en la carpeta: {carpeta_salida}\n")

if __name__ == "__main__":
    main()
