# Backend de Rollacard

## Descripción
Rollacard es una app...

## Instalación del proyecto
1. Una vez clonado el proyecto, mediante consola dirijirse a la carpeta raíz del proyecto.
2. Crear un entorno virtual con `virtualenv`
3. Activar el entorno virtual `source ./.venv/bin/activate`
4. Instalar los requierimientos necesarios `pip install -r requirements.txt`
5. Configurar el archivo .env con las variables de entorno que se usarán:
```
ENV_GUNICORN_CMD=
ENV_GUNICORN_DIR=
ENV_GUNICORN_USR=
```
6. Ejecutar:
```
set -a
source ./.env
set +a
```
7. Ejecutar para arrancar el proyecto `.venv/bin/supervisord -c supervisord.conf` 
8. Verificar en http://127.0.0.1:8000
9. Crear las migraciones `python manage.py makemigrations`
10. Ejecutar las migraciones `python manage.py migrate`
11. Cargar los datos base:
```
python manage.py loaddata scr/preload.json
python manage.py load_family_words
```