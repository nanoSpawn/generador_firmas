# -*- coding: utf-8 -*-

#Python 3.5
#Importamos dependencias
import csv
import jinja2
import argparse
import sys
import pathlib


#FUNCIONES

#Definimos la función que hace las listas automáticas
#Argumentos: d, cadena que especifica el nombre de la carpeta
def listado(d):

    #Creamos el diccionario de firmas usando el CSV, el formato del archivo es:
    #1.Filename   2.Nombre    3.Email
    #Todo separado por comas. El formato está en la primera línea.

    #nota: El bucle se ejecuta dentro de la llamada de creación del diccionario
    with open('listafirmas.txt', mode='r') as csv_file:
        listafirmas = csv.DictReader(csv_file)
    
    #Creamos los html con este bucle
        count = 0;

        for row in listafirmas:
            filename = d+row['filename']+".html"
            print(filename)
            html = template.render(name=row["name"], email=row["email"])
            with open(filename, "w+") as f:
                f.write(html)
                count += 1
                f.close()
    print('Se han creado',count,'firmas')
    print('Recuerdo que es posible crear firmas individuales. Usar -h o --help para información')
    
#Definimos la función para firmas sueltas
#Los argumentos son los de la línea de comandos:
#Filename, Name, Email y Directory
def firma(fn,n,e,d):
    
    if fn==None and n!=None:
        fn = n
    elif fn==n==None:
        sys.exit('Se debe especificar al menos nombre o nombre de archivo')
    
    #Si no hemos especificado algo, lo ponemos en blanco.
    if n==None: n=''
    if e==None: e=''
    
    html = template.render(name=n, email=e)
    with open(d+fn+'.html', "w+") as f:
        f.write(html)
        f.close()
    
    print('Se ha creado la firma '+fn)

#FIN DE FUNCIONES

#Creamos el entorno de Jinja2 para usarlo luego. Esta es la librería
#que parsea el HTML y nos hace la vida más fácil
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template('firma.html')

#Capturamos argumentos si los hubiera. El funcionamiento del script debe
#ser como sigue:
# a) No hay argumentos. Se hace la listafirmas.txt entera.
# b) Hay argumentos. Se parsean y se crea la firma específica.
# Argumentos: 
# --filename / -f : Nombre del fichero html, si se omite se usa el nombre
# --name / -n : Nombre
# --email / -e : Email
# --help / -h : Imprime la ayuda.

filename = ''
name = ''
email = ''

parser = argparse.ArgumentParser(
    description='Script que genera firmas de correo a partir de una plantilla html. Puede o bien coger las firmas de un archivo CSV o bien aceptar argumentos para crear una firma individualizada.')
parser.add_argument('-f', '--filename', action='store', dest='filename', help='Nombre del fichero html. Si se omite se usará el nombre de la persona especificado en -n')
parser.add_argument('-n', '--name', action='store', dest='name', help='Nombre a mostrar en el mail. Si se hace necesario poner espacios en el nombre, usar comillas.')
parser.add_argument('-e', '--email', action='store', dest='email', help='Email')
parser.add_argument('-d', '--directory', action='store', dest='directory', help='Carpeta en la que guardar las firmas. Por defecto será /Firmas Automaticas/')

args = parser.parse_args()
filename=args.filename
name=args.name
email=args.email

#Si solo queremos cambiar la carpeta, hemos de añadir la condición.
#Lo hacemos ahora antes de poner el default.
if filename==name==email==None and args.directory != None:
    newfolder = True
else:
    newfolder = False

#Ponemos el valor default si no especificamos uno nosotros
if args.directory != None: 
    directory = args.directory+'/'
else:
    directory='firmas automaticas/'
    
#Si la carpeta no existiera, la creamos ahora.
#Es poco elegante, pero usar una subcarpeta evita problemas como 
#machacar la plantilla HTML.
pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


#Y a crear las firmas, si no hay argumentos o solo se pasa la carpeta, se hacen todas.
#Si hay argumentos se crea la firma personalizada.
if not len(sys.argv) > 1 or newfolder:
    listado(directory)
else:
    firma(filename, name, email, directory)

#Cerramos el script y el intérprete, para evitar que se queden sesiones abiertas
sys.exit()