#!/bin/bash
apt-get update && apt-get install -y build-essential python3-dev gfortran
pip install --upgrade pip setuptools
pip install -r requirements.txt
