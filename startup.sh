#!/bin/bash
set -euo pipefail

LOG=/home/LogFiles/startup.log
exec >> "$LOG" 2>&1
echo "Running startup.sh..."

python manage.py migrate --noinput || echo "migrate failed (non-fatal)"

echo "Starting Gunicorn on PORT=${PORT:-8000}"
exec gunicorn christy_portfolio.wsgi:application \
  --bind=0.0.0.0:${PORT:-8000} \
  --workers=1 --threads=2 \
  --timeout=120 --graceful-timeout=120 --keep-alive=5 --log-level=info
