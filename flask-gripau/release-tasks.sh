#!/bin/bash
echo "Running release tasks"
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
python add_data.py
echo "Finished release tasks"