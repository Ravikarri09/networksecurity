from setuptools import setup, find_packages
from typing import List
def get_requirements()->List[str]:
    """ This fuction will return the list of requirements"""
    requirement_list=[]

    try:
        with open('requirements.txt','r') as file:
            ###read lines from file
            lines=file.readlines()
            ###process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list
###setting up the meta data
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Karri Ravi  Shankar",
    author_email="ravishankar.karri2005Agmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)




