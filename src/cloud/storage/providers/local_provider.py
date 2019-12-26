import os
import shutil
from .base_provider import BaseProvider

class LocalProvider(BaseProvider):

    __bucket = None
    __connection = None

    def __init__(self, host, port, user=False, password=False):
        self.host = host
        self.port = port

    def upload(self, bucket, filename, destination):
        """
        Uploads a file to a local folder and return the complete destination path
        
        Parameters
        ----------
        bucket : str, the base folder to storage the files
        filename: str, the source base path for the uploaded file like a/path/with/file.txt
        destination: str, the destination path a/destination/folder/path/new_name_file.txt
        return 
        """

        destination_path = self.__get_file_path(destination)
        destination_file_name = os.path.join(bucket, destination)
        if os.path.isfile(filename) and self.exists(bucket, destination_path):
            return shutil.copyfile(filename, destination_file_name)
        else:
            raise Exception('The filepath does not exists')

    def download(self, butcket, filename, destination):
        raise NotImplementedError()

    def exists(self, bucket, filename):
        path_to_check = os.path.join(bucket, filename)
        if os.path.isdir(path_to_check):
            return True
        elif os.path.isfile(path_to_check):
            return True
        return False

    def mkdir(self, bucket, path):
        path_to_create = os.path.join(bucket, path)
        if os.path.isdir(path_to_create):
            raise Exception('Path already exists')
        else:
            os.mkdir(path_to_create)

            return path_to_create

    def pwd(self):
        return os.path.curdir()

    def cwd(self, directory):
        return os.chdir(directory)

    def quit(self):
        raise NotImplementedError()
