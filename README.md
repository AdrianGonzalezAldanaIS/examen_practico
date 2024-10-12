## Instrucciones de como ejecutar los proyectos System_library y Tareas_api

Primero, el archivo lectura_texto.py se puede ejecutar normalmente desde VSC o en terminal con terminal "python lectura_texto.py", el archivo llamado texto.txt debe estar en la misma carpeta que lectura_texto.py
Segundo, el archivo ordenamiento.py se puede ejecutar normalmente desde VSC o en terminal con terminal "python ordenamiento.py".
Tercero, el archivo consulta_MySQL.txt tiene las querys desde como se crea un bd en MySQL hast las inserciones que se pidieron


Dentro de la carpeta dj se encuentran los dos sistemas que se pidieron en el examen práctico, en ambos sistemas llamdo System_Library se debe de crear un entorno virtual, 


1.- esto se hace con el siguiente comando "python -m venv env"

2.- Se debe activar con env\Scripts\activate, si se activo bien el prompt debe lucir así 
(env) C:\Users\Usuario....

3.- Después, debe de entrar a la carpeta System_Library con el comando cd System_Library

4.- Ya realizado lo anterior se deb de instalar todas las dependencias que se ocuparon con el comando "pip install -r requeriments.txt"

5.- Al final para ejecutar el sistema se debe de hacer con el comando "python manage.py runserver"


Para el sistema Tareas_api realizar los puntos 3, 4, y 5

Para System_Library cuando ya esta en ejecucuión ir a tu navegador y poner lo siguiente http://127.0.0.1:8000/, después agregar admin/ al final, debe quedar así http://127.0.0.1:8000/admin/

User: admin
Password: admin

Para Tareas_api cuando ya esta en ejecucuión ir a tu navegador y poner lo siguiente http://127.0.0.1:8000/, después agregar api/ al final, debe quedar así http://127.0.0.1:8000/api/tareas, se mostraran dos tareas, si quieres consulta por id se debe poner http://127.0.0.1:8000/api/tareas/1 o http://127.0.0.1:8000/api/tareas/2 y ahí te indica si quieres actualiza o borrarlo. El crud es más dinámico
