# BlogArticulos (sistema_coder)

+ Este proyecto es una aplicación web de Django. A continuación se describen los pasos necesarios para instalar y ejecutar el proyecto en un entorno local:

## Instalación
+ Crea una carpeta madre en tu computadora
+ Abre una terminal y navega hasta la carpeta madre
+ Crea un ambiente virtual y actívalo. Puedes usar virtualenv o conda, por ejemplo.
+ Clona este repositorio dentro de la carpeta madre.
+ En la terminal, navega hacia la carpeta del proyecto que acabas de clonar
+ Instala las dependencias usando el siguiente comando:

```
pip install -r requirements.txt
```

## Acceder al panel administrativo
### Para acceder al panel administrativo de Django, sigue los siguientes pasos:
+ En la terminal, crea un superusuario usando el siguiente comando:
```
python manage.py createsuperuser
```
+ Abre un navegador web y escribe la siguiente dirección:
```
127.0.0.1:8000/admin
```
+ Ingresa las credenciales del superusuario que creaste en el paso anterior.
+ Con esto deberías estar listo para explorar y probar la aplicación. ¡Que disfrutes!