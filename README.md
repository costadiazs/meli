						MercadoLibre - Ejercicio Mails

Este documento describe cómo ejecutar el script para buscar y cargar en la base de datos todos los mails que contengan la palabra “DevOps” en el Subject de una cuenta específica.

Los prerrequisitos son los siguientes:

- Docker/Docker Compose
- Cargar datos(mail, password) del mail a inspeccionar. Tener en cuenta que en caso de usar verificación de dos pasos Gmail solo permite acceder desde afuera con contraseñas de aplicaciones, ver siguiente link  https://support.google.com/mail/answer/185833?hl=es

Instalacion ::
- Instalar Docker-compose
- Cargar los parametros email & password en credentials.py
- Desde cualquier consola verificar la instalación de docker mediante el siguiente comando	
        Docker-compose --version
- Una vez que tenemos docker-compose instalado correctamente ejecutamos el siguiente comando desde la carpeta del proyecto
	Docker-compose up
- Cuando termine de correr el docker-compose se habran cargado los mails en la base de datos mysql
- Verificar los datos(base de datos/ registros en la tabla EMAIL) cargados desde la pagina localhost:8080 accediendo con las siguientes credenciales
        user :: root
        password :: root
		

