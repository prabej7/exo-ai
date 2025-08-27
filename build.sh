#!/bin/bash
set -e

echo "Upgrading pip and setuptools..."
python -m pip install --upgrade pip setuptools wheel

echo "Setting environment variables..."
export PIP_NO_CACHE_DIR=1
export PIP_USE_PEP517=0
export PIP_DISABLE_PIP_VERSION_CHECK=1

echo "Installing dependencies with legacy resolver..."
pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

echo "Build completed successfully!"
