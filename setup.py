import os
from setuptools import setup, find_packages



def read(*path):
    """ r
    Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>>read("README.md")
    ...
    """

    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *path)
    with open(filepath)as file_:
        return file_.read().lstrip  
    
def read_requirements(path):
    """return a list of requirements from a text file"""
    return [
        line.strip ()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]

setup(
    name="dundie",
    version="0.1.0",
    description="Rewards Point System for Dunder Mifflin",
    author="Marcelo de Moura",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    },
    installrequires=read_requirements("requeriments.txt"),
    extras_require={
        "test": read_requirements("requeriments.test.txt"),
        "dev": read_requirements("requeriments.dev.txt")
    }

)
