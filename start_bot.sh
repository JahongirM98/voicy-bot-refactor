#!/bin/bash
/wait-for-it.sh db:5432 -t 60
exec python interfaces/bot/main.py

