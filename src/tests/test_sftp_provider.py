import os
import unittest
import builtins
from ftplib import FTP, FTP_TLS
from unittest import mock, TestCase
from cloud.storage.file_system import FileSystem

class TestSftpProvider(TestCase):

    def setUp(self):
        self.user = 'user'
        self.password = 'password'
        self.host = 'localhost'
        self.port = 22
        self.__prepare_enviroment()

        super(TestSftpProvider, self).setUp()

    @mock.patch('cloud.storage.providers.sftp_provider.pysftp.Connection')
    def test_download_from_sftp_server(self, sftp_connection_constructor_mock):
        destination = 'a/folder/to_download/'
        remote_path_to_download = "%s%s%s" %(self.__butcket_to_test, os.sep, self.__file_name_to_test)
        sftp_connection = FileSystem('sftp', self.__login_arguments)
        sftp_connection.download(self.__butcket_to_test, self.__file_name_to_test, destination)

        sftp_connection_instance_mock = sftp_connection_constructor_mock.return_value
        
        sftp_connection_constructor_mock.assert_called_with(self.host,
                                                            username=self.user,
                                                            password=self.password)
        
        sftp_connection_instance_mock.get.assert_called_with(remote_path_to_download, destination)
    
    @mock.patch('cloud.storage.providers.sftp_provider.pysftp.Connection')
    def test_upload_to_sftp_server(self, sftp_connection_constructor_mock):
        file_path_to_upload ='a{0}path{0}to{0}upload{0}'.format(os.sep) 
        
        expected_destination_path = "%s%s%s" % (self.__butcket_to_test, os.sep, file_path_to_upload)
        expected_uploaded_path = 'sftp://%s:%s@%s:%s/%s' % (self.user, self.password, self.host, self.port, expected_destination_path.replace('\\', '/'))
        
        sftp_connection = FileSystem('sftp', self.__login_arguments)
        file_loaded_url = sftp_connection.upload(self.__butcket_to_test, file_path_to_upload + self.__file_name_to_test, file_path_to_upload)

        sftp_connection_instance_mock =  sftp_connection_constructor_mock.return_value
        sftp_connection_constructor_mock.assert_called_with(self.host,
                                                            username=self.user,
                                                            password=self.password)

        sftp_connection_instance_mock.put.assert_called_with(file_path_to_upload + self.__file_name_to_test, expected_destination_path + self.__file_name_to_test)

        self.assertEqual(expected_uploaded_path, file_loaded_url)
        
    def __prepare_enviroment(self):
        self.__butcket_to_test = 'a_bucket'
        self.__file_name_to_test = 'a_file.txt'
        self.__login_arguments = {'host': self.host,
                                  'port': self.port,
                                  'user': self.user,
                                  'password': self.password
                                  }
