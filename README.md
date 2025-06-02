### Proyecto de Automatización para la Extracción de Sitios de Unión de Factores de Transcripción en *E. coli* en Experimentos de ChIP-Seq

---

### Resumen

Este proyecto tiene como objetivo automatizar el proceso de identificación del sitio exacto de unión de los reguladores transcripcionales para **144 factores de transcripción (TFs)** en el genoma completo de *Escherichia coli*.  
Las regiones de unión de estos TFs se han determinado mediante la técnica **ChIP-Seq**.

---

###Datos Disponibles

#### Archivo de Picos  
**`union_peaks_file.tsv`**

Contiene información sobre las regiones de unión de los 144 TFs. Las columnas incluidas son:

- `Dataset_Ids`: Identificadores del dataset por experimento o condición.
- `TF_name`: Nombre del factor de transcripción.
- `Peak_start`: Posición inicial del pico de unión.
- `Peak_end`: Posición final del pico.
- `Peak_center`: Posición central del pico.
- `Peak_number`: Número secuencial del pico dentro del dataset.
- `Max_Fold_Enrichment`: Enriquecimiento máximo observado.
- `Max_Norm_Fold_Enrichment`: Enriquecimiento máximo normalizado.
- `Proximal_genes`: Genes próximos al sitio de unión.
- `Center_position_type`: Tipo de posición del centro del pico (e.g., intergénica, intrónica, etc.).

####Genoma Completo de *E. coli*  
Disponible en formato **FASTA** como:  
**`E_coli_K12_MG1655_U00096.3.txt`**

---

### Objetivos del Proyecto

#### Generación de Archivos FASTA

Desarrollar un programa que extraiga y compile las **secuencias de picos** para cada TF en archivos individuales en formato **FASTA**.  
Cada archivo representará un regulador específico.

---

### Buenas Prácticas de Desarrollo

- **Control de Versiones**: Uso de *Git* para la gestión de cambios y colaboración.
- **Revisión de Código**: Revisión periódica para mejorar calidad y compartir conocimientos.
- **Documentación Exhaustiva**: Manual detallado del código y procesos.
- **Pruebas Automatizadas**: Validación constante de funcionalidad y robustez.

---

### Plan de Implementación

1. **Desarrollo del Extractor de Secuencias**  
   Automatización del proceso que genera archivos FASTA desde el archivo TSV de picos.

2. **Integración y Pruebas**  
   Integración de módulos y pruebas integrales para validar funcionalidad.

3. **Implementación de la Librería Argparse**  
   Uso de argumentos de línea de comandos para mayor flexibilidad del usuario.

