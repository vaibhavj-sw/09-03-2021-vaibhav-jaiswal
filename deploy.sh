#!/usr/bin/env bash

source ./venv_bmi/bin/activate
pip install -r requirements.txt
rm -rf output.csv
python main.py