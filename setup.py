from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    
    """
    requirement_lst : list[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
               requirement = line.strip()

               if requirement and requirement != "-e .":
                   requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

# print(get_requirements())

setup(
    name="NETWORKSECURITY", 
    version="0.0.1",
    author="Chaitanya Shrimali",
    author_email="chaitanyashrimali7322@gmail.com",
    packages=find_packages(),   
    install_requires=get_requirements(),
)
