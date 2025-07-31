#!/bin/bash
LOG=/home/LogFiles/startup.log

# Redirect output to log file with timestamps
exec >> $LOG 2>&1
exec > >(while read -r line; do echo "$(date '+%Y-%m-%d %H:%M:%S') $line"; done) 2>&1

echo "Running startup.sh..."

pip install --upgrade pip
pip install -r requirements.txt

# Wait for the database to be ready
until python manage.py migrate; do
  echo "Database not ready. Retrying in 5 seconds..."
  sleep 5
done

python manage.py collectstatic --noinput

echo "Starting Gunicorn on \$PORT=${PORT:-8000}"
exec gunicorn christy_portfolio.wsgi:application --bind=0.0.0.0:${PORT:-8000} --timeout 600