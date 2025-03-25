#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Configure Streamlit
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

echo "Setup complete"
