#!/bin/bash
set -e

echo "Updating system and installing dependencies..."
apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

echo "Upgrading pip, setuptools, and wheel..."
pip3 install --upgrade pip setuptools wheel

echo "Installing project dependencies..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

echo "Environment setup complete!"
