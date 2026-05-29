from setuptools import setup, find_packages 
#it will find all the packages in the current directory and subdirectories(__init__.py files are required in each package)

from typing import List 
#Declaring variables for setup functions
#PROJECT_NAME = "housing-predictor"

def get_requirements() -> List[str]:
    """
    Description: This function is going to return list of requirements mentioned in requirements.txt file
    """
    requirements_lst: List[str] = []
    try:
        #open the requirements.txt file in read mode
        with open("requirements.txt", "r") as requirement_file:
            #read the requirements.txt file and return a list of requirements
            lines = requirement_file.readlines()
            #strip the lines and return a list of requirements
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirements_lst


setup(    
      name="NetworkSecurity_meta",
      version="0.0.1",
      author="Vijay",
      author_email="vijaybalaji235@gmail.com",
      description="A package for Network Security",
      packages=find_packages(),
      install_requires=get_requirements()
)