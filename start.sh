#!/bin/bash
ENV_PATH=$1

# Carga las variables de entorno desde el archivo .env
set -a
source "$ENV_PATH"
set +a

cd ${ENV_GUNICORN_DIR}
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Ejecutar supervisord u otros comandos necesarios
.venv/bin/supervisord -c supervisord.conf

