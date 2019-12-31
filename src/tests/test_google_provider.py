import os
import unittest
import builtins
from google.cloud import storage
from unittest import mock, TestCase
from cloud.storage.file_system import FileSystem


class TestGoogleProvider(TestCase):

    def setUp(self):
        self.__prepare_enviroment()
        super(TestGoogleProvider, self).setUp()

    @mock.patch('cloud.storage.providers.google_provider.storage.Client.from_service_account_json')
    def test_download_from_google_cloud(self, mock_google_connection_service):
        a_google_key_path = 'a/path/to/key.json'
        destination = 'a/folder/to_download/'
        user_config = {'google_cloud_storage_key_path':a_google_key_path}
        
        mock_blob_manager = self.__prepare_google_mock(mock_google_connection_service)
        
        file_system = FileSystem('google', user_config)
        file_system.download(self.__butcket_to_test, self.__file_name_to_test, destination)
        
        mock_google_connection_service.assert_called_with(a_google_key_path)
        mock_blob_manager.download_to_filename.assert_called_with(destination)

    @mock.patch('cloud.storage.providers.google_provider.storage.Client.from_service_account_json')
    def test_upload_to_google_cloud(self, mock_google_connection_service):
        a_google_key_path = 'a/path/to/key.json'
        destination_to_upload = 'a/folder/to_upload/'
        user_config = {'google_cloud_storage_key_path':a_google_key_path}
        mock_blob_manager = self.__prepare_google_mock(mock_google_connection_service)
        
        file_system = FileSystem('google', user_config)
        file_system.upload(self.__butcket_to_test, self.__file_name_to_test, destination_to_upload + self.__file_name_to_test)

        mock_google_connection_service.assert_called_with(a_google_key_path)
        mock_blob_manager.upload_from_filename.assert_called_with(self.__file_name_to_test)
    
    def __prepare_enviroment(self):
        self.__butcket_to_test = 'a_bucket'
        self.__file_name_to_test = 'a_file.txt'
    
    def __prepare_google_mock(self, mock_google_connection_service):
        mock_bucket = mock.create_autospec(storage.Bucket)
        mock_blob_manager = mock.create_autospec(storage.Blob)
        mock_blob_manager.download_to_filename.return_value = True

        mock_bucket.blob.return_value = mock_blob_manager
        
        instance_client = mock_google_connection_service.return_value
        instance_client.get_bucket.return_value = mock_bucket

        return mock_blob_manager
   
if __name__ == '__main__':
    unittest.main()
