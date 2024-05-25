#!/bin/bash
# Asume que el primer argumento es la ruta al archivo .env
ENV_PATH=$1


# Carga las variables de entorno desde el archivo .env
set -a
source "$ENV_PATH"
set +a

source ${ENV_GUNICORN_CMD}/activate

# Continuar con la instalación de requisitos y ejecución de supervisord
pip install -r ${ENV_GUNICORN_DIR}/requirements.txt
${ENV_GUNICORN_CMD}/supervisord -c ${ENV_GUNICORN_DIR}/supervisord.conf

