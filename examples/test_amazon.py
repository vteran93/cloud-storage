import os
from cloud.storage import file_system

AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')

config = {
            'aws_access_key': AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': AWS_SECRET_ACCESS_KEY
        }

fs = file_system.FileSystem('amazon', config)
fs.upload('houselandbucket', 'testing.jpg', '2020/01/01/testing.jpg')
fs.download('houselandbucket', '2020/01/01/testing.jpg', 'mydownload.jpg')
