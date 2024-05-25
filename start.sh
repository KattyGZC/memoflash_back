#!/bin/bash
ENV_PATH=$1

# Carga las variables de entorno desde el archivo .env
set -a
source "$ENV_PATH"
set +a

sudo chown -R $USER:$USER /home/kattyko_gzc/memoflash_back
sudo chmod -R 755 /home/kattyko_gzc/memoflash_back

cd ${ENV_GUNICORN_DIR}
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Comprobar si supervisord está en ejecución
PID=$(pgrep -f supervisord)

if [ "$PID" ]; then
    echo "Supervisord is running with PID: $PID, shutting it down..."
    supervisorctl stop all
    supervisorctl shutdown
else
    echo "Supervisord is not running."
fi

# Esperar un momento para asegurarse de que todos los procesos se han detenido
sleep 5

# Iniciar supervisord
echo "Starting supervisord..."
.venv/bin/supervisord -c supervisord.conf

# Mostrar el estado de los procesos
supervisorctl status

