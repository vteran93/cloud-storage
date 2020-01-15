import os
import shutil
from copy import copy
from queue import deque
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
        
        Returns
        -------
        destination path
            The path where the new file it is
        """
        destination_path = self.get_file_path(destination)
        destination_file_name = os.path.join(bucket, destination)

        if not os.path.isfile(filename):
            raise Exception('The source file does not exists')
        elif not self.exists(bucket, destination_path):
            self.mkdir(bucket, destination_path)
            return self.upload(bucket, filename, destination)
        else:
            return shutil.copyfile(filename, destination_file_name)

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
            self.__build_path(path_to_create)

            return path_to_create

    def __build_path(self, requested_path):
        path_parts = deque(requested_path.split(os.sep))
        new_path_parts = copy(path_parts)
        for folder in path_parts:
            if os.path.exists(folder):
                self.cwd(folder)
            else:
                os.mkdir(folder)
                new_path_parts.popleft()
                return self.__build_path(os.sep.join(path_parts))

    def pwd(self):
        return os.path.curdir()

    def cwd(self, directory):
        return os.chdir(directory)

    def quit(self):
        raise NotImplementedError()