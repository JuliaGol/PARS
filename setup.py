#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()
    
requirements = ['beautifulsoup4>=4.9.3', 'biopython>=1.79', 'setuptools>=50.3.0','requests~=2.25.1', 'bs4>=0.0.1']


setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Julia Gołębiowska, Adam Cicherski, Patrycja Owczarek",
    author_email='je.golebiowska@student.uw.edu.pl',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Project which enable automatic downloading data from pfam and rfam databases",
    entry_points={
        'console_scripts': [
            'PARS=PARS.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='PARS',
    name='PARS',
    packages=['pars'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/JuliaGol/PARS',
    project_urls={"Bug Tracker":"https://github.com/JuliaGol/PARS/issues"},
    version='0.1.1',
    zip_safe=False,
)
