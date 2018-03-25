from setuptools import setup, find_packages
from os import path

root = path.abspath(path.dirname(__file__))

with open(path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tenx_missile',
    version='0.0.1',
    description='Python driver to control the Tenx USB Missile Launcher',
    long_description=long_description,
    url='https://github.com/anxodio/tenx-missile',
    author='Àngel Fernández',
    author_email='angelfernandezibanez@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['pyusb'],
)
