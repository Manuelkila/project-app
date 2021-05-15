import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-idowuscrumy',
    version =0.1,
    packages = find_packages(),
    include_package_data = True,
    license = "BSD License",
    description = 'A simple django app that says hello world',
    long_description = README,
    url = 'http://127.0.0.1:8000/idowuscrumy',
    author = 'Idowu Kila',
    author_email = 'emmanuelkila1@gmail.com',
    classifiers = [
        'Environment :: web environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2.3',
        'Intendend Audience :: Developers',
        'License :: OSI Approved :: BS License',
        'Operating System :: OS Independent', 
        'Programming Language :: Python',
        'Programmning Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        

    ]

)