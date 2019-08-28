from setuptools import setup, find_packages

setup(
    name='pycalc',
    description='pure-python command line calculator',
    version='0.0.1',
    author='Konstantsin Tratseuski',
    author_email='kostya04.11.1998@gmail.com',
    packages=find_packages(),
    entry_points='''
    [console_scripts]
    pycalc = pycalc.pycalc:main
    '''

)
