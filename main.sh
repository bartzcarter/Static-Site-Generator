#!/bin/bash

# Run the Python script to generate the site
python3 src/main.py

# Navigate to the public directory
cd public || exit

# Start a simple HTTP server on port 8888
python3 -m http.server 8888