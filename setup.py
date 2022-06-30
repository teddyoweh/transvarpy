from setuptools import setup

setup(
   name='transvar',
   version='0.1.0',
   author='teddyoweh',
   author_email='teddy@teddyoweh.net',
   packages=['package_name', 'package_name.test'],
   scripts=['Ttransvar/__init__.py'],
   url='http://pypi.python.org/pypi/transvar/',
   license='LICENSE.txt',
   description='A new method of declaring and editing variable names',
   long_description=open('README.md').read(),
    keywords=[ 'transvar','python transvar','python', 'python variables','variables'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)