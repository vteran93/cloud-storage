import os
import unittest
import builtins
from ftplib import FTP, FTP_TLS
from unittest import mock, TestCase
from cloud.storage.file_system import FileSystem
from cloud.storage.providers.ftp_provider import FtpProvider


class TestFtpProvider(TestCase):

    def setUp(self, *args, **kwargs):
        self.host = 'localhost'
        self.port = 21
        self.user = 'my_user'
        self.password = 'my_password'
        self.tls_secure = True
        self.__prepare_enviroment()
        
        super(TestFtpProvider, self).setUp()

    @mock.patch('cloud.storage.providers.ftp_provider.FTP_TLS', autospec=True)
    @mock.patch('builtins.open', create=True)
    def tests_ftp_with_tls_download_file(self, mock_writer, mock_ftp_constructor):
        expected_ftp_command = 'RETR %s%s%s' % (self.__butcket_to_test, os.sep, self.__file_name_to_test)
        mock_ftp_instance = self.__prepare_mock_ftp_instance(mock_ftp_constructor.return_value)
        mock_ftp_instance.retrbinary.return_value = True

        self.__file_system = FileSystem('ftp_tls', self.__login_arguments)
        self.__file_system.download(self.__butcket_to_test, self.__file_name_to_test, 'a_destination')
        
        mock_ftp_constructor.assert_called_with(self.host)
        mock_ftp_instance.login.assert_called_with(self.user, self.password)
        mock_ftp_instance.retrbinary.assert_called_with(expected_ftp_command, mock_writer.return_value.write)

    @mock.patch('cloud.storage.providers.ftp_provider.FTP_TLS', autospec=True)
    @mock.patch('builtins.open', create=True)
    def tests_ftp_with_tls_upload_file(self, mock_reader, mock_ftp_constructor):
        destination_folder = 'a_destination'
        expected_ftp_command = 'STOR %s%s%s'% (self.__butcket_to_test, os.sep, destination_folder)
        mock_ftp_instance = self.__prepare_mock_ftp_instance(mock_ftp_constructor.return_value)
        mock_ftp_instance.storbinary.return_value = True

        self.__file_system = FileSystem('ftp_tls')
        self.__file_system.upload(self.__butcket_to_test, self.__file_name_to_test, destination_folder)

        mock_ftp_constructor.assert_called_with(self.host)
        mock_ftp_instance.login.assert_called_with(self.user, self.password)
        mock_ftp_instance.storbinary.assert_called_with(expected_ftp_command, mock_reader.return_value)

    def __prepare_enviroment(self):
        self.__butcket_to_test = 'a_bucket'
        self.__file_name_to_test = 'a_file.txt'
        self.__login_arguments = {'host': self.host,
                           'port': self.port,
                           'user': self.user,
                           'password': self.password,
                           'tls': self.tls_secure}

    def __prepare_mock_ftp_instance(self, mock_ftp_instance):
        mock_ftp_instance.login.return_value = True
        mock_ftp_instance.prot_p.return_value = True

        return mock_ftp_instance


if __name__ == '__main__':
    unittest.main()
