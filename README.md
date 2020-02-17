# Generador de firmas
## Generador automático de firmas de correo a partir de un CSV y una plantilla HTML.

Script realizado en Python 3.5

Se ejecuta directamente y guarda en la carpeta "firmas automaticas" (podría ser necesario crearla de antemano) los HTML generados a partir de un archivo CSV, usando la plantilla.

Puede crear firmas individuales usando la línea de comandos.

  **-h, --help**        Muestra la ayuda
  
  **-f FILENAME, --filename** 
                        Nombre del fichero html. Si se omite se usará el
                        nombre de la persona especificado en -n
                        
  **-n NAME, --name**   Nombre a mostrar en el mail. 
                        Si se hace necesario poner espacios en el nombre, usar comillas.
  
  **-e EMAIL, --email** Email

Dependencias: csv, Jinja2.

En este repositorio hay archivos de ejemplo para la plantilla y la lista de firmas.
