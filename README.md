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
| `FrameWorks`             |  [Reflex](https://reflex.dev/ "Reflex")               |
| `Motor de base de datos` | MySQL , PostgreSQL , Sqlite3                          |

# Pasos de instalación

##### 1) Descomprimir el proyecto en una carpeta de tu sistema operativo

##### 2) Preparando un entorno virtual para el proyecto

Linux:

```bash
apt-get install -f -y python3-pip python3-venv 
.
mkdir /path/proyecto
cd /path/proyecto
.
python3 -m venv .venv
source .venv/bin/activate
.
python3 -m pip install pip --upgrade 
python3 -m pip install Django==5.1.2
.
django-admin startproject core .
.
python3 manage.py runserver
http://127.0.0.1:8000/
CONTROL-C
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py startapp apis
.
```

##### 3) Instalar librerias del proyecto

```bash
python3 -m pip install -r requirements.txt
```

##### 4) Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")
Linux debes instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador.

##### 5) Inicializar el proyecto

```bash
python3 manage.py runserver
```

##### 6) Iniciar la app del proyecto

```bash
python3 manage.py runserver
```

##### 7) Iniciar sesión en el sistema

```bash

http://127.0.0.1:8000/admin
.
username: admin
password: IchiBan
```

------------

#  Gracias por su atencion ✅🙏

***KSM, 2024.***

