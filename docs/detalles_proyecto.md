# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

Fecha:11/03/2025

Participantes: 

- [Dulce Alejandra Carrillo Carlos]  <email:carrillo@lcg.unam.mx > 

## Descripción del Problema
<!-- Puedes empezar con una introducción, luego la justificación y plantear el problema. -->

El propósito de este proyecto es automatizar el proceso de extracción y análisis de regiones genómicas donde se lleva a cabo la unión de factores de transcripción en Escherichia coli. Para ello, se dispone de un archivo con los sitios de unión identificados y otro con la secuencia completa del genoma. La meta es generar archivos FASTA específicos para cada factor de transcripción, que contengan las secuencias correspondientes a sus sitios de unión. Posteriormente, estas secuencias serán analizadas con el programa MEME para descubrir motivos regulatorios. Para facilitar este análisis, se desarrollará un script en shell que ejecute automáticamente MEME con los archivos FASTA generados para cada factor.

## Especificación de Requisitos

1. **Requisitos Funcionales**

**A. Validación de formato de archivos**

- Implementar una función que revise si los archivos de entrada tienen el formato correcto antes de iniciar el análisis.

**B. Generación de Archivos FASTA a partir de sitios de unión**

**Input:**

El programa deberá aceptar como parámetros desde la línea de comandos los siguientes elementos:

- Archivo con la información de los sitios de unión para distintos factores de transcripción
- FASTA con la secuencia completa del genoma de *E. coli*.
- Argumento adicional que indique el directorio de destino donde se guardarán los archivos generados.

**Extracción de Secuencias:**

- A partir del archivo de picos, se deben identificar las coordenadas de inicio y fin correspondientes a los sitios de unión de cada TF (TF_name).
- Usando estas coordenadas, se deben extraer las secuencias específicas desde el archivo genómico FASTA, considerando únicamente la forward strand. 
- Es obligatorio verificar que las coordenadas se encuentren dentro de los límites del genoma; de no ser así, se debe notificar el error con un mensaje claro al usuario.

**Output (FASTA):**

- Para cada TF_name, se debe generar un archivo en formato FASTA nombrado según el identificador del factor de transcripción y almacenar en el directorio de salida esperado. 
- En caso de que un mismo TF_name aparezca en más de un experimento, se debe incluir el Dataset_Id correspondiente en el nombre del archivo para evitar ambigüedades.

---

**C. Automatización del Análisis de Motivos**

**Input:**

- Directorio que contenga los archivos FASTA generados previamente, cada uno con las secuencias de unión correspondientes a un TF.

**Script:**

- El programa debe recorrer todos los archivos FASTA dentro del directorio proporcionado.
- Para cada archivo, se debe construir una línea de instrucción que invoque el software MEME con los parámetros adecuados para realizar el análisis de motivos.
- Se debe crear un script en shell (`meme.sh`) que contenga todas las instrucciones para ejecutar MEME sobre cada uno de los archivos FASTA.

---

2. **Requisitos No Funcionales**

**Facilidad de Uso y documentación:**

- El sistema debe ser compatible con Linux, MAC y Windows. 
- La ejecución será desde la línea de comandos
- El código debe implementarse utilizando Python y/o scripts en shell.
- Debe existir un manual de uso accesible que descirba como usarlo y enliste posibles problemas y como solucionarlos.
- Todo el código debe estar debidamente comentado y acompañado de documentación clara.

**Software:**

- Se deberá utilizar un sistema de control de versiones para documentar y revisar el desarrollo del proyecto.
- Es necesario realizar pruebas que validen el correcto funcionamiento del sistema.

**Diseño Modular:**

- El código debe estar organizado en módulos o funciones bien definidos, de forma que cada componente (extracción, validación, análisis, generación de script) pueda mantenerse y modificarse por separado.

## Análisis y Diseño

<!-- Incluir el algoritmo o pseudocódigo. También puedes usar casos de uso, u otros diagramas UML. Como sugerencia dar solución requisito por requisito. Describir formatos de datos de entrada y salida. -->





