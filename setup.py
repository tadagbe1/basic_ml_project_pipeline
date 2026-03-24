from setuptools import find_packages, setup

from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of the packages
    """
    
    with open(file_path, 'r') as file_obj:
        packages = file_obj.readlines()
        packages = [package.replace('\n', '') for package in packages]
    if HYPEN_E_DOT in packages:
        packages.remove(HYPEN_E_DOT)
    return packages


setup(
    name='mlproject',
    version='0.0.1',
    author='tadagbe',
    author_email='tadagbedhossou@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)