from setuptools import setup, find_packages

setup(
    name = 'fortdep',
    version = '170612',
    description = 'generates dependencies between Fortran source files to include in Makefile',
    url = 'https://github.com/gronki/fortdep',
    author = 'Dominik Gronkiewicz',
    author_email = 'gronki@gmail.com',
    license = 'MIT',
    py_modules = ['fortdep'],
    entry_points = {
        'console_scripts': [
            "fortdep = fortdep:main"
        ]
    }
)
