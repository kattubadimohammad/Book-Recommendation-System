#!/bin/bash
# Install necessary dependencies
apt-get update && apt-get install -y build-essential python3-dev gfortran

# Upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

# Install project requirements
pip install -r requirements.txt
