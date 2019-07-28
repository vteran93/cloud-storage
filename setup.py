import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='images-uploader',  
     version='0.1',
     scripts=[''] ,
     author="Victor Francisco Teran Herrera",
     author_email="vteran93@yahoo.es",
     description="A package to control uploads and downloads from diference platforms",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://bitbucket.org/houselandbog/imagesuploader",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )