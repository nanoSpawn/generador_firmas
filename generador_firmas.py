# -*- coding: utf-8 -*-

#Python 3.5
#Importamos dependencias
import csv
import jinja2
import argparse
import sys

#FUNCIONES

#Definimos la función que hace las listas automáticas
def listado():

    #Creamos el diccionario de firmas usando el CSV, el formato del archivo es:
    #1.Filename   2.Nombre    3.Email
    #Todo separado por comas. El formato está en la primera línea.

    #nota: El bucle se ejecuta dentro de la llamada de creación del diccionario
    with open('listafirmas.txt', mode='r') as csv_file:
        listafirmas = csv.DictReader(csv_file)
    
    #Creamos los html con este bucle
        count = 0;

        for row in listafirmas:
            filename = "firmas automaticas/"+row['filename']+".html"
            print(filename)
            html = template.render(name=row["name"], email=row["email"])
            with open(filename, "w+") as f:
                f.write(html)
                count += 1
                f.close()
    print('Se han creado',count,'firmas')
    print('Recuerdo que es posible crear firmas individuales. Usar -h o --help para información')
    
#Definimos la función para firmas sueltas    
def firma(fn,n,e):
    
    #Creamos una firma suelta, tan fácil como coger la plantilla, y aplicar valores
    
    #Si no hemos especificado algo, lo ponemos en blanco.
    
    if n==None: n=''
    if e==None: e=''
        
    
    if fn==None and n!=None:
        fn = n
    elif fn==n==None:
        print('Se debe especificar al menos nombre o nombre de archivo')
        exit()
    
    html = template.render(name=n, email=e)
    with open('firmas automaticas/'+fn+'.html', "w+") as f:
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

args = parser.parse_args()
filename=args.filename
name=args.name
email=args.email


if not len(sys.argv) > 1:
    listado()
else:
    firma(filename, name, email)





    
    
    