#!/bin/bash
set -e

# Update and install build dependencies
apt-get update && apt-get install -y build-essential python3-dev gfortran

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install project requirements
pip install -r requirements.txt
