from setuptools import find_packages,setup
from typing import List


Hyp = "-e ."
def get_requirments(file_path:str)->List[str]:
    
    """
    this function wil return list of requirments
    """

    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [ req.replace("\n","") for req in requirments]

        if Hyp in requirments:
            requirments.remove(Hyp)

    return requirments

setup(
name = "ML-project",
version = '0.0.1',
author = "Archit",
author_email = "pragyesharchit8@gmail.com",
packages = find_packages(),
install_requires = get_requirments("requirments.txt")


)