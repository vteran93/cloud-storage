import unittest
from unittest.mock import MagicMock
from ftplib import FTP, FTP_TLS
from cloud.storage.providers.ftp_provider import FtpProvider


class TestFtpProvider(unittest.TestCase):

    def test_upload_ftp_with_tls(self):

        host='localhost'
        port=21
        user='my_user'
        password='my_password'

        FtpProvider(host, port, user, password)
        ftp_mock = FTP()
        ftp_mock.connect = MagicMock(return_value=True)
        ftp_mock.storbinary = MagicMock(return_value=True)

    def test_upload_ftp_without_tls(self):
        pass

    def test_download_ftp_with_tls(self):
        pass

    def test_download_ftp_without_tls(self):
        pass

if __name__ == '__main__':
    unittest.main()