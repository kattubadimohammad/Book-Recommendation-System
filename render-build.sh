#!/bin/bash
set -e

echo "Updating system and installing dependencies..."
apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-venv \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

echo "Creating and activating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

echo "Installing project dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

echo "Environment setup complete!"
