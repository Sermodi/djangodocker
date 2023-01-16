import os
import re
#Script que reescribe los archivos para que el docker se ejecute correctamente.
#Pedir nombres de la app, base de datos, etc

#APPName={APPName}
#WEBPORT={WEBPORT}
#DBNAME={DB}
#DBUSER={DBUser}
#DBPASSWD={DBPass}
#DBPORT={DBPORT}

def main():
    APPName=""
    print("Este script se encargará de modificar los archivos para poder ejecutar el Docker de Django con los parámetros deseados: nombre, base de datos, puertos...")
    print("Cualquier duda o consulta puede efectuarse por correo a programacion@enoges.com o por github: Sermodi")
    #Se pide el nombre del proyecto
    while len(APPName) > 10 or APPName == "":
        APPName = input("\t-->Escribe el NOMBRE ABREVIADO DEL PROYECTO, como máximo 10 caracteres, sin caracteres especiales.\n\tNombre: ")
        if len(APPName) > 10:
            print("Recuerda que el nombre debe tener máximo de 10 caracteres.\n")

        if not re.match("^[A-Za-z0-9]+$", APPName):
            print("Por favor, que el nombre no incluya caracteres especiales como: -_*!·$%&/@()=?...\n")
            APPName = ""
    #Se pide el nombre de la base de datos.
    dbname = ""
    while len(dbname) > 10 or dbname == "":
        dbname = input("\t-->Escribe el NOMBRE DE LA BASE DE DATOS, como máximo 10 caracteres, sin caracteres especiales.\n\tDB Name: ")
        if len(dbname) > 10:
            print("Recuerda que el nombre debe tener máximo de 10 caracteres.\n")

        if not re.match("^[A-Za-z0-9]+$", dbname):
            print("Por favor, que el nombre no incluya caracteres especiales como: -_*!·$%&/@()=?...\n")
            dbname = ""
    #Se pide el nombre de usuario
    dbuser = ""
    while len(dbuser) > 15 or dbuser == "":
        dbuser = input("\t-->Escribe el nombre de USUARIO DE LA BASE DE DATOS, como máximo 15 caracteres, sin caracteres especiales.\n\tDB User: ")
        if len(dbuser) > 15:
            print("Recuerda que el nombre debe tener máximo de 10 caracteres.\n")

        if not re.match("^[A-Za-z0-9]+$", dbuser):
            print("Por favor, que el nombre no incluya caracteres especiales como: -_*!·$%&/@()=?...\n")
            dbuser = ""
    #Se pide la contraseña de la base de datos
    dbpasswd = ""
    while len(dbpasswd) < 6 or dbpasswd == "":
        dbpasswd = input("\t-->Escribe la CONTRASEÑA DE LA BASE DE DATOS, como mínimo 6 caracteres y un carácter especial.\n\tDB Password: ")
        if len(dbpasswd) < 6:
            print("Recuerda que la contraseña debe tener como mínimo 6 caracteres.\n")
        #Comprobamos si la contraseña tiene un carácter especial
        if not re.search("[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", dbpasswd):
            print("Recuerda que la contraseña debe tener al menos un carácter especial.\n")
            dbpasswd = ""
    
    #Se pide el puerto de la base de datos
    dbport = 0
    while not(int(dbport)>0 and int(dbport)<65535):
        dbport = input("\t-->Escribe el PUERTO DE LA BASE DE DATOS, debe ser un número entre 0 y 65535.\n\tDB Port: ")
        if not(int(dbport)>0 and int(dbport)<65535):
            print("Recuerda que el puerto debe ser un número entre 0 y 65535.\n")
            dbport = 0

    #Se pide el puerto de la web
    webport = 0
    while not(int(webport)>0 and int(webport)<65535):
        webport = input("\t-->Escribe el PUERTO DE LA WEB, debe ser un número entre 0 y 65535.\n\tWEB Port: ")
        if not (int(webport)>0 and int(webport)<65535):
            print("Recuerda que el puerto debe ser un número entre 0 y 65535.\n")
            webport = 0

    #Se pide la URL de la imagen docker
    imageUrl = ""
    while imageUrl == "":
        imageUrl = input("\t-->Escribe la URL DE LA IMAGEN DOCKER para descargarla, como por ejemplo: 'ghcr.io/sermodi/djangodocker:latest'.\n\tURL: ")
        if imageUrl == "":
            print("Recuerda que la URL no puede estar vacía.\n")
    
    
    #hacemos un print de los datos aportados
    print("Los datos introducidos son los siguientes:\n")
    print("Nombre del proyecto: "+APPName)
    print("Nombre de la base de datos: "+dbname)
    print("Nombre de usuario de la base de datos: "+dbuser)
    print("Contraseña de la base de datos: "+dbpasswd)
    print("Puerto de la base de datos: "+dbport)
    print("Puerto de la web: "+webport)
    print("URL de la imagen docker: "+imageUrl)
    #Escriba "y" para confirmar los datos
    confirm = input("Si los datos son correctos, escriba 'y' para confirmarlos.\n")
    if confirm != "y":
        print("Se cerrará el script, puede volver a ejecutarlo cuando quiera.\n")
        exit()
    #copiamos los archivos de configFiles a la carpeta del proyecto, asi evitamos archivos modificados
    shresult = os.popen('cp configFiles/* .')
    shresult = os.popen('cp configFiles/.* .')

    #Creamos la carpeta oldFiles
    shresult = os.popen('mkdir oldFiles')
    #Copiamos el archivo .env a la carpeta oldFiles
    shresult = os.popen('cp .env oldFiles/.env')
    #Copiamos el archivo docker-compose.yml a la carpeta oldFiles
    shresult = os.popen('cp docker-compose.yml oldFiles/docker-compose.yml')
    #Copiamos los archivos .sh a la carpeta oldFiles
    shresult = os.popen('cp *.sh oldFiles/')

    #Modificación del archivo .env 
    #cambiamos {WEBPORT} por el puerto de la web
    shresult = os.popen('sed -i "s/{WEBPORT}/' + str(webport) + '/g" .env')
    #cambiamos {DBPORT} por el puerto de la base de datos
    shresult = os.popen('sed -i "s/{DBPORT}/' + str(dbport) + '/g" .env')
    #cambiamos {DB} por el nombre de la base de datos
    shresult = os.popen('sed -i "s/{DB}/' + str(dbname) + '/g" .env')
    #Cambiamos {DBPass} por la contraseña de la base de datos
    shresult = os.popen('sed -i "s/{DBPass}/' + str(dbpasswd) + '/g" .env')
    #cambiamos {DBUser} por el nombre de usuario de la base de datos
    shresult = os.popen('sed -i "s/{DBUser}/' + str(dbuser) + '/g" .env')
        
    #Modificación del archivo docker-compose.yml
    #cambiamos {APPName} por el nombre del proyecto
    shresult = os.popen('sed -i "s/{APPName}/' + str(APPName) + '/g" docker-compose.yml')
    #cambiamos el ImageUrl por la URL de la imagen docker
    shresult = os.popen('sed -i "s|{ImageUrl}|' + str(imageUrl) + '|g" docker-compose.yml')

    #Modificación de los archivos .sh
    #cambiamos {APPName} por el nombre del proyecto
    shresult = os.popen('sed -i "s/{APPName}/' + str(APPName) + '/g" *.sh')
    
    #Una vez modificados los archivos se informa de los cambios realizados.
    print("· Se han realizado los cambios en los archivos .env, docker-compose.yml y los archivos .sh.\n")
    print("· Se ha creado la carpeta oldFiles con los archivos antiguos.\n")
    print("· Se ha creado el proyecto con el nombre: "+APPName+"\n")

    print("\t -- Se procede a crear la carpeta app con el proyecto Django -- \n")
    #Se crea la carpeta app
    shresult = os.popen('mkdir app')
    #Se pregunta al usuario si quiere descargar el proyecto de github o crear un proyecto nuevo.
    print("¿Desea descargar el proyecto de github o crear un proyecto nuevo?\n")
    print("1. Descargar proyecto de github.")
    print("2. Crear proyecto nuevo.")
    print("3. Salir.")
    option = 0
    while not(int(option)>0 and int(option)<4):
        option = input("Escriba el número de la opción que desea: ")
        if not (int(option)>0 and int(option)<4):
            print("Recuerda que la opción debe ser un número entre 1 y 3.\n")
            option = 0
    if option == "1":
        #Se pide la URL del proyecto de github
        githubUrl = ""
        while githubUrl == "":
            githubUrl = input("Escriba la URL del proyecto de github, como por ejemplo: 'https://github.com/Applica2/ejemplo-webapp.git'")
            if githubUrl == "":
                print("Recuerda que la URL no puede estar vacía.\n")
        #Se descarga el proyecto de github
        shresult = os.popen('git clone ' + githubUrl + ' gitcloned')
        #Se mueve el proyecto a la carpeta app
        shresult = os.popen('mv gitcloned/* app/')
        #Se borra la carpeta gitcloned
        shresult = os.popen('rm -r gitcloned')
    if option == "2":
        #Se crea el proyecto Django
        shresult = os.popen('cd app; python3 -m django startproject ' + APPName + ' .')
        import time
        time.sleep(1.5)
    if option == "3":
        print("Se cerrará el script, puede volver a ejecutarlo cuando quiera.\n")
        exit()


    
if __name__ == "__main__":
    main()