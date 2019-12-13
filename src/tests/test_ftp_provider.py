import builtins
from ftplib import FTP, FTP_TLS
from unittest import mock, TestCase
from cloud.storage.file_system import FileSystem
from cloud.storage.providers.ftp_provider import FtpProvider

class TestFtpProvider(TestCase):

    def setUp(self, *args, **kwargs):
        self.host='localhost'
        self.port=21
        self.user='my_user'
        self.password='my_password'
        self.tls_secure = True
        super(TestFtpProvider, self).setUp()

    @mock.patch('cloud.storage.providers.ftp_provider.FTP_TLS', autospec=True)
    @mock.patch('builtins.open', create=True)
    def tests_upload_ftp_with_tls(self, mock_writer, mock_ftp_constructor):
        mock_ftp_instance = mock_ftp_constructor.return_value
        
        self.__file_system = FileSystem('ftp_tls', {'host': self.host, 'port':self.port, 'user':self.user, 'password':self.password, 'tls':self.tls_secure})
        self.__file_system.download('abucket', 'a_file', 'a_destination')
        
        mock_ftp_instance.login.return_value = True
        mock_ftp_instance.prot_p.return_value = True
        mock_ftp_instance.retrbinary.return_value = True

        self.assertTrue(mock_ftp_instance.login.called)
        self.assertTrue(mock_ftp_instance.retrbinary.called)


if __name__ == '__main__':
    unittest.main()