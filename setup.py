from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Bansi Patel"
DESCRIPTION="This is first machine learning project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requiremnets mention
    in requiremnets.txt file

    return this function is going to return a list which contains name of
    libraries mentioned in requiremnets.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requiremnet_file:
        requiremnet_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)