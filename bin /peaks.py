import os
import pandas as pd

def leer_archivo_picos(peaks_archivo):
    if not os.path.isfile(peaks_archivo):
        raise FileNotFoundError(f"El archivo de picos no se encontró: {peaks_archivo}")
    
    try:
        df = pd.read_csv(peaks_archivo, sep="\t")
        required = {"TF_name", "Peak_start", "Peak_end"}
        if not required.issubset(df.columns):
            raise ValueError(f"Faltan columnas necesarias en el archivo: {required - set(df.columns)}")
        
        picos = []
        for _, fila in df.iterrows():
            try:
                picos.append({
                    "TF_name": str(fila["TF_name"]),
                    "start": int(float(fila["Peak_start"])),
                    "end": int(float(fila["Peak_end"]))
                })
            except Exception as e:
                print(f"[WARN]: Pico inválido omitido - {e}")
        return picos
    except Exception as e:
        raise ValueError(f"Error al leer el archivo de picos: {e}")
