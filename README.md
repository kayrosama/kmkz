# KMKZ
(NOTA: Aun en construccion)
Sistema de control enfocado al sector de comercio informal.
Este proyecto inicia con la necesidad de crear controles para empresas en formacion.

Se tiene contemplado la implementacion de los modulos:
- Inventario
- Track de Paquetes / Cajas
- Arendamiento de Servicios

# Pasos para instalar el Sistema

# Instaladores
| Nombre                   | Instalador                                            |
|:-------------------------|:------------------------------------------------------| 
| `Compilador`             | Python3                                               |
| `IDE de programación`    | Visual Studio Code , Sublime Text , Atom , Vim , etc. |
| `FrameWorks`             |  [Django](https://www.djangoproject.com/ "Django") ,  [Django REST](https://www.django-rest-framework.org/ "Django REST")              |
| `Motor de base de datos` | MySQL , PostgreSQL , Sqlite3                          |

##### Pasos de instalación

Linux:

```bash

git clone https://github.com/kayrosama/kmkz.git
cd kmkz
apt-get install -f -y python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt 

```

NOTA 01: 
Al llegar a este punto, debes eliminar todas las miigraciones registradas en la aplicacion y preparar la base de datos. 
Si fuera Sqlite3 habra que eliminar el archivo db.sqlite3.
En nuestro caso hemos descidido utiliar PostgreSQL sobre Docker.

```bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
http://127.0.0.1:8000/
CONTROL-C

```
NOTA 02:
Al cambiar la base de datos, es necesario volver a crear el super usuario por lo que debera comentar las lineas [ USERNAME_FIELD = 'email' y REQUIRED_FIELDS = [] ] en el archivo [user/models.py](user/models.py).

```bash

python3 manage.py createsuperuser

```

Ahora ejecutamos las migraciones.
Levantamos el servicio.
Validamos el cambio realizado.

```bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
http://127.0.0.1:8000/
CONTROL-C

```

##### 1) Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")
Linux debes instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador.

##### 2) Sugerencia para crear el super usuario en aplicacion

```bash

http://127.0.0.1:8000/admin

username: admin
password: kasama

```

------------

#  ありがとう

***KSM, 2024.***

