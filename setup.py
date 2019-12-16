# -*- coding: utf-8 -*-
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='cloud-storage',
    version='0.1',
    #scripts=[''],
    author="Victor Francisco Teran Herrera",
    author_email="vteran93atyahoo.es",
    description="A package to control uploads and downloads from different platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'google-api-core',
        'google-auth',
        'google-cloud-core',
        'google-cloud-storage',
        'google-resumable-media',
        'googleapis-common-protos',
        'isort',
        'lazy-object-proxy',
        'mccabe',
        'paramiko',
        'protobuf',
        'pyasn1',
        'pyasn1-modules',
        'PyNaCl',
        'pysftp',
        'urllib3',
        'wrapt',
        'nose'
    ],
    url='https://bitbucket.org/houselandbog/cloud-storage',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
