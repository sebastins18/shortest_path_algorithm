"""
Este archivo de configuración de setuptools se utiliza para empaquetar y distribuir el Proyecto_1.
Define las dependencias del proyecto, puntos de entrada y otros metadatos relevantes.
"""

from setuptools import setup, find_packages

setup(
    name='Proyecto_1',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest==6.2.5',
        'pylint==2.11.1',
        'numpy',
        'matplotlib',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'proyecto_1 = src.main:main',
        ],
    },
)
