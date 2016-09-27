# SignRequest client for Python

Unofficial python client for SignRequest's API.

Currently only supports two features I needed for a specific proof of concept:

- Create document from base64 encoded file content
- Sending signature requests for a document

If I somehow continue using this I will include tests and other features.

## Features

Create document from base64 encoded document content:

```python
import base64

from signrequest import SignRequest

sr = SignRequest('API_KEY')

with open('/tmp/pdf-sample.pdf', 'rb') as file:
    file_encoded_string = base64.b64encode(file.read())

doc = sr.create_document(file=file_encoded_string,
                         document_id='pdf_sample',
                         document_name='pdf-sample.pdf')
```

Send signature request for the document created in step one:

```python
sr.send_sign_request(from_email='john@johnssohn.com',
                     message='Please sign this thing.',
                     signers='james@jamessohn.com') # Can also be an array of emails
```

You can also send a document without creating it first if you got an URL, for that specify it as argument when calling method for sending a sign request:

```python
from signrequest import SignRequest

document = 'https://signrequest.com/api/v1/documents/c27f3e0b-616a-4a74-9182-c00d4e3aa16a/'
sr = SignRequest('API_KEY').send_sign_request(document=document,
                                              from_email='john@johnssohn.com',
                                              message='Please sign this thing.',
                                              signers=['a@eiou.com', 'z@yz.com'])
```
