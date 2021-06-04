import os
import setuptools

setuptools.setup(
    name="ansible_specdoc",
    version="0.0.1",
    author="Lena Garber",
    author_email="lbgarber2@gmail.com",
    description=("A simple tool for generating Ansible collection documentation from module spec."),
    license="GNU General Public License v3.0",
    keywords="ansible",
    url="http://packages.python.org/ansible-specdoc",
    packages=['ansible_specdoc'],
    install_requires=[
        'PyYAML==5.4.1'
    ],
    python_requires='>=3.6',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['ansible_specdoc=ansible_specdoc.cli:main']
    }
)