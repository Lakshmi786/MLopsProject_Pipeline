'''
the setup file is an essential part of packaging and distributing python projects.
It is used by setuptools to define the configuration of your project, such as its metadata, dependecies
and more.
'''

from setuptools import find_packages,setup
from typing import List


requirement_lst :List[str] = []

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    try:
        with open('requirements.txt','r') as file:
            #Read lines form the file
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author = "Lakshmi",
    author_email="@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
