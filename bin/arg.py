import os
import argparse

def parsear_argumentos():
    parser = argparse.ArgumentParser(
        description= "Procesa el genoma y los picos para generar archivos FASTA por TF.")
    
    parser.add_argument(
        "--genoma", "-fa",
        type=str,
        default=os.path.join("data", "E_coli_K12_MG1655_U00096.3.txt"),
        help= "Ruta al archivo del genoma en formato FASTA."
    )

    parser.add_argument(
        "--picos", "-tsv",
        type=str,
        default=os.path.join("data", "union_peaks_file.tsv"),
        help= "Ruta al archivo con los picos en formato TSV."
    )

    parser.add_argument(
        "--salida", "-o",
        type=str,
        default="results",
        help= "Carpeta de salida para los archivos FASTA."
    )

    return parser.parse_args()
