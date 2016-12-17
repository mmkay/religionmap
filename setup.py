import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-religionmap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'overpass',
        'django-jsonify'
    ],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app to show religion data.',
    long_description=README,
    url='http://www.mmkay.pl/',
    author='Mateusz Kulewicz',
    author_email='mateusz.kulewicz+religionmap@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
