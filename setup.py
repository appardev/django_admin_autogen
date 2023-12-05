# setup.py
from setuptools import setup, find_packages

setup(
    name='django-autogen-admin',
    version='0.1',
    description='A Django package to dynamically create admin classes. Including all fields in a model, or all models in an app.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='sean@appar.com.tw',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',  # Make sure to specify appropriate versions
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update with your chosen license
    ],
)
