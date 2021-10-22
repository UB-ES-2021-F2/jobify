#!/bin/bash
rm -r migrations
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
python add_data.py