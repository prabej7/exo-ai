#!/bin/bash
set -e

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Setting pip to use legacy resolver..."
export PIP_USE_PEP517=0

echo "Installing dependencies..."
pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

echo "Build completed successfully!"
