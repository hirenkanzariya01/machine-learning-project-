from setuptools import setup, find_packages

def get_requirements(path:str)->list[str]:
  with open(path) as p:
    requirements = p.readlines()
    requirements = [req.replace('\n', '') for req in requirements]
    return requirements

setup(
  name='Machine Learning Project',
  version=0.0.3, 
  author='Hiren Knzariya',
  author_email='hirenkanzariya655@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)