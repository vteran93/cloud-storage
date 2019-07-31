class StorageError(IOError):pass

class UnableToUploadFile(StorageError): pass

class UnableToDownload(StorageError):pass

class UnableToLogin(StorageError):pass