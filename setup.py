from setuptools import setup

setup(
   name='transvarpy',
   version='0.1.0',
   author='teddyoweh',
   author_email='teddy@teddyoweh.net',
   packages=['transvarpy'],
   scripts=['transvarpy/__init__.py'],
   license='LICENSE.txt',
   maintainer_email='teddyoweh@teddyoweh.net',
   maintainer='teddyoweh',
   url='https://github.com/teddyoweh/transvarpy/',
   
   description='A new method of declaring and editing variable names',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
    keywords=[ 'transvarpuy','python transvar','python', 'python variables','variables'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)