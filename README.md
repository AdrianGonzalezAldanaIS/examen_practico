##Instrucciones de como ejecutar los proyectos System_library y Tareas_api

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
