from setuptools import setup, find_packages

setup(
    name="nasa-space-app-api",
    version="1.0.0",
    description="NASA Space App Challenge 2025 API",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.2.5",
        "numpy>=1.23.5",
        "scikit-learn>=1.2.2",
        "joblib>=1.2.0",
        "gunicorn>=20.1.0",
    ],
    python_requires=">=3.11",
    include_package_data=True,
)
