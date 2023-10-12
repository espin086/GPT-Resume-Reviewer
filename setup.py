#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="JJ Espinoza",
    author_email='jj.espinoza.la@gmail.com',
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
    description="GPT-Resume-Reviewer is a repository that contains a machine learning model trained on GPT (Generative Pre-trained Transformer) to review and analyze resumes. It provides an automated way to evaluate resumes based on various criteria such as skills, experience, and qualifications.",
    entry_points={
        'console_scripts': [
            'gpt_resume_reviewer=gpt_resume_reviewer.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gpt_resume_reviewer',
    name='gpt_resume_reviewer',
    packages=find_packages(include=['gpt_resume_reviewer', 'gpt_resume_reviewer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/espin086/gpt_resume_reviewer',
    version='0.0.1',
    zip_safe=False,
)
