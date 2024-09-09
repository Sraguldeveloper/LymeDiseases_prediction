from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    return requirements
            
    
setup(
    name="Lyme disease prediction",
    version="0.0.1",
    author="Ragul",
    author_email="gunkemail622@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement('requirement.txt')
)