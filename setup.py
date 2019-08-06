import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='images-uploader',
    version='0.1',
    scripts=[''],
    author="Victor Francisco Teran Herrera",
    author_email="vteran93@yahoo.es",
    description="A package to control uploads and downloads from diference platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'google-api-core==1.14.2',
        'google-auth==1.6.3',
        'google-cloud-core==1.0.3',
        'google-cloud-storage==1.17.0',
        'google-resumable-media==0.3.2',
        'googleapis-common-protos==1.6.0',
        'isort==4.3.21',
        'lazy-object-proxy==1.4.1',
        'mccabe==0.6.1',
        'paramiko==2.6.0',
        'protobuf==3.9.0',
        'pyasn1==0.4.6',
        'pyasn1-modules==0.2.6',
        'PyNaCl==1.3.0',
        'pysftp==0.2.9',
        'urllib3,
        'wrapt==1.11.2',
    ],
    url="https://bitbucket.org/houselandbog/imagesuploader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
