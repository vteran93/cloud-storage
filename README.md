# images-uploader

Dependencia para cargar imagenes de acuerdo al driver.

## LICENCE
<cloud-storage>  Copyright (C) <2020>  <Victor Teran Herrera>

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions


# Punto de entrada

clase ImagesController

Tiene los métodos

- Upload
- Download
- Exist
- mkdir
- pwd
- quit

Mediante polimorfismo debe poder acceder a uno de las clases de control especificas

- Google Cloud Storage
- FTP
- SFTP
- Amazon Web Services s3
- Local

Para acceder, se instancia desde la clase ConnectionProvider de acuerdo a la parametria de la clase, la clase correcta y se devuelve la instancia

Dependencias

- google.cloud.storage
- pysftp
- boto3 Amazon Simple Storage Service 
- ftplib

Para generar el coverage con ejecución de las pruebas unitarias

```bash
$ nosetests-3.4.exe --with-coverage --cover-package=cloud.storage --cover-html
```