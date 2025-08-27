#!/bin/bash
set -e

echo "Checking Python version..."
python --version

echo "Forcing Python 3.11..."
if command -v python3.11 &> /dev/null; then
    echo "Python 3.11 found, using it..."
    PYTHON_CMD="python3.11"
else
    echo "Python 3.11 not found, using default python..."
    PYTHON_CMD="python"
fi

echo "Upgrading pip and setuptools..."
$PYTHON_CMD -m pip install --upgrade pip setuptools wheel

echo "Setting environment variables..."
export PIP_NO_CACHE_DIR=1
export PIP_USE_PEP517=0
export PIP_DISABLE_PIP_VERSION_CHECK=1

echo "Installing dependencies with legacy resolver..."
$PYTHON_CMD -m pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

echo "Build completed successfully!"
