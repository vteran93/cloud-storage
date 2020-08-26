# -*- coding: utf-8 -*-
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='cloud-storage',
    version='0.1',
    author="Victor Francisco Teran Herrera",
    author_email="vteran93atyahoo.es",
    description="A package to control uploads and downloads from different platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'bcrypt==3.2.0',
        'boto3==1.4.4',
        'botocore==1.5.95',
        'cachetools==4.1.1',
        'certifi==2020.6.20',
        'cffi==1.14.2',
        'chardet==3.0.4',
        'cloud-storage==0.1',
        'cryptography==3.0',
        'docutils==0.16',
        'google-api-core==1.22.1',
        'google-auth==1.20.1',
        'google-cloud-core==1.4.1',
        'google-cloud-storage==1.30.0',
        'google-crc32c==1.0.0',
        'google-resumable-media==1.0.0',
        'googleapis-common-protos==1.52.0',
        'idna==2.10',
        'isort==5.4.2',
        'jmespath==0.10.0',
        'lazy-object-proxy==1.5.1',
        'mccabe==0.6.1',
        'nose==1.3.7',
        'paramiko==2.7.1',
        'protobuf==3.13.0',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycodestyle==2.6.0',
        'pycparser==2.20',
        'pyflakes==2.2.0',
        'PyNaCl==1.4.0',
        'pysftp==0.2.9',
        'python-dateutil==2.8.1',
        'pytz==2020.1',
        'requests==2.24.0',
        'rsa==4.6',
        's3transfer==0.1.13',
        'six>=1.12.0',
        'toml==0.10.1',
        'urllib3==1.25.10',
        'wrapt>=1.12.1',
    ],
    url='https://bitbucket.org/houselandbog/cloud-storage',
    #package_dir={'': ''},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
