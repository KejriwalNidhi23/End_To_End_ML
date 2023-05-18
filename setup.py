from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    print(file_path)
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML_Project',
    version='0.0.1',
    author = 'Nidhi',
    author_email = 'kejriwal.nidhi23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)