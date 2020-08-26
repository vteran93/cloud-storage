
from .base_provider import BaseProvider

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


class AmazonProvider(BaseProvider):

    def __init__(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        self.__connection = boto3.client('s3',
                                         aws_access_key_id=kwargs['aws_access_key'],
                                         aws_secret_access_key=kwargs['aws_secret_access_key'])

    def upload(self, bucket, filename, destination):
        try:
            self.__connection.upload_file(filename, bucket, destination)
        except NoCredentialsError as identifier:
            raise identifier

        file_url = '%s/%s/%s' % (self.__connection.meta.endpoint_url,
                                 bucket,
                                 destination)

        return file_url

    def download(self, bucket, filename, destination):
        try:
            self.__connection.download_file(bucket, filename, destination)
        except Exception as identifier:
            raise identifier

    def exists(self, bucket, filename):
        try:
            self.__connection.head_object(Bucket=bucket, Key=filename)
            return True
        except ClientError as identifier:
            if identifier.response['Error']['Code'] != '404':
                return False
        return False

    def mkdir(self, bucket, path):
        raise NotImplementedError()

    def pwd(self):
        raise NotImplementedError()

    def cwd(self):
        raise NotImplementedError()

    def quit(self):
        raise NotImplementedError()
