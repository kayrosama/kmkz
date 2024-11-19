# APIBASE
(NOTA: Aun en construccion)
Cascaron de APIS con CRUD de usuarios para partir de este codigo.

# Pasos para instalar el Sistema

# Instaladores
| Nombre                   | Instalador                                            |
|:-------------------------|:------------------------------------------------------| 
| `Compilador`             | Python3                                               |
| `IDE de programación`    | Visual Studio Code , Sublime Text , Atom , Vim , etc. |
| `FrameWorks`             |  [Django](https://www.djangoproject.com/ "Django") , [Django REST](https://www.django-rest-framework.org/ "Django REST")               |
| `Motor de base de datos` | MySQL , PostgreSQL , Sqlite3                          |

##### Secuencia para instalación levantar la aplicacion

Linux:

```bash

git clone https://github.com/kayrosama/ksm.git
cd ksm
apt-get install -f -y python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt 

```

En el archivo model debes encontrar estas variables y comentarlas.

```bash

users/models.py

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

```

Eliminar la base de datos creada [db.sqlite3] y todas los archivos 00###_xxxx.py registradas en los directorios mitrations en cada aplicacion y posteriormente ejecutar las nuevas migraciones.

```bash

python3 manage.py makemigrations
python3 manage.py migrate

```

Mientras esta aun este desarrollando el proyecto se debe crear un super usuario con credenciales faciles de recordar.  Se muestra sugerencia para crear el super usuario de aplicacion.

```bash

python3 manage.py createsuperuser

username: admin
email: master@ksm.io
password: adm123

```

Antes de levantar el servicio y probar el super usuario creado, debe de descomentrar las variables que comento.

```bash

users/models.py

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

...

python3 manage.py runserver

http://127.0.0.1:8000/admin
email: master@apibase.com
password: adm123

```

------------

#  ありがとう

***KSM, 2024.***

