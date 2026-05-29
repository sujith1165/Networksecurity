'''The set.py file is an essential part of packageing and distributing Python projects. It contains metadata about the project
, such as its name, version, author, and dependencies. This information is used by tools like pip to install the package and 
manage its dependencies. The setup.py file also defines the entry points for the package, allowing users to run the package's 
functionality from the command line. Overall, the setup.py file is crucial for ensuring that a Python project can be easily
 installed and used by '''

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    requirements_lst: List[str] = []

    try:
        with open("requirements.txt") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # ignore empty lines and editable install
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_lst


setup(
    name="Networksecurity",
    version="0.0.1",
    author="Sujith",
    author_email="sujithkumar.sr1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)