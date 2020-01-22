# -*- coding: utf-8 -*-

#Python 3.5
#Importamos dependencias
import csv
import jinja2

#Creamos el entorno de Jinja2 para usarlo luego. Esta es la librería
#que parsea el HTML y nos hace la vida más fácil
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template('firma.html')

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
    
    