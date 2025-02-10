from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    
    Dot = "-e ."
    requirements=[]
    with open('requirements.txt') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if Dot in requirements:
            requirements.remove(Dot)
        
    return requirements


    
    
    setup(
        name='Backpack Prediction Challenge',
        version='0.0.1',
        author='Naman',
        author_email='namankumar4499@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt')
    )