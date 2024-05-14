# trabajoLabSE
 Trabajo de la asignatura de Laboratorio de Sistemas Empotrados

# Introduccion
Este trabajo se ha realizado a partir del que fue desarrollado por Adrián Alcolea 
y Javier Resano, donde se presenta un acelerador basado en FPGA para el algoritmo 
de Gradient Boosting Decision Trees (GBDT). 
Este enfoque se centra en optimizar la implementación del algoritmo GBDT utilizando 
hardware reconfigurable, con el objetivo de mejorar significativamente el 
rendimiento en términos de velocidad de procesamiento y eficiencia energética 
en comparación con implementaciones tradicionales basadas en CPU o GPU. El acelerador propuesto utiliza técnicas avanzadas de paralelismo y optimización de recursos 
para lograr un rendimiento superior, lo que demuestra el potencial de las FPGA 
en aplicaciones de aprendizaje automático y procesamiento de datos intensivos .

Partiendo de este trabajo, mi investigación se centra en una optimización adicional 
del diseño original, específicamente en la reducción del tamaño de la palabra de 
estado. La palabra de estado es una parte crucial del diseño de FPGA, ya que 
determina la cantidad de memoria utilizada y, por ende, el espacio disponible para 
otras operaciones y funcionalidades. Al reducir el tamaño de esta palabra de estado, 
se puede disminuir el uso de memoria en la FPGA, lo que no solo libera recursos 
para aumentar las prestaciones del sistema, sino que también mejora la eficiencia 
general del acelerador. Esta optimización es esencial para aprovechar al máximo 
las capacidades del hardware reconfigurable y mejorar aún más el rendimiento del 
acelerador en aplicaciones de aprendizaje automático.

# Descripcion de la implementacion

# Analisis de los nodos

## Como se ha reducido

# Resultados obtenidos

# Bibliografia
Trabajo de Adrián Alcolea:
https://www.mdpi.com/2079-9292/10/3/314

Codigo y tests:
https://github.com/universidad-zaragoza/FPGA_accelerator_for_GBDT/tree/main

# Derechos de autor
```
@Article{Alcolea2021FPGAforGBDT,
    AUTHOR         = {Alcolea, Adrián and Resano, Javier},
    TITLE          = {FPGA Accelerator for Gradient Boosting Decision Trees},
    JOURNAL        = {Electronics},
    VOLUME         = {10},
    YEAR           = {2021},
    NUMBER         = {3},
    ARTICLE-NUMBER = {314},
    URL            = {https://www.mdpi.com/2079-9292/10/3/314},
    ISSN           = {2079-9292},
    DOI            = {10.3390/electronics10030314}
}
```
