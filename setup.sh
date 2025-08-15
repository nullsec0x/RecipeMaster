#!/bin/bash
PORT=$1

if [ -z "$PORT" ]; then
    echo "Usage: $0 <PORT>"
    exit 1
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

gunicorn --workers 3 --bind unix:/home/nullsec0x/.recipemaster.nullsec0x.hackclub.app.webserver.sock app:app
