import base64
import binascii
import json
import uuid

import requests

DOCUMENTS_URL = 'https://signrequest.com/api/v1/documents/'
SIGN_REQUESTS_URL = 'https://signrequest.com/api/v1/signrequests/'


class SignRequest:

    def __init__(self, api_token):
        self.api_token = api_token
        self.document = None
        pass

    def _get_request_headers(self):
        '''Builds headers for HTTP request.'''
        headers = {'Authorization': 'Token {}'.format(self.api_token),
                   'Content-Type': 'application/json'}
        return headers

    def create_document(self, file=None, document_id=None, document_name=None):
        '''Creates a SignRequest document using a base64 encoded file, and actual file or a publicly
        available URL for a file. Document name including extension is required for string encoded
        files.'''
        if not document_id:
            raise Exception('Document ID is required')
        # We're duck testing if it's a file, URL or base64 encoded string with file
        # Source: https://goo.gl/tNxyt3
        file_is_string_encoded = False
        try:
            base64.decodestring(file)
            data_key = 'file_from_content'
            file_is_string_encoded = True
            if not document_name:
                raise Exception('Document name required when file is an encoded string')
        except binascii.Error as e:
            # For now only base 64 encoded string is supported
            # todo: URL and file duck testing, assigning data_key
            pass

        data = {data_key: file, 'external_id': document_id}

        if file_is_string_encoded:
            data['file_from_content_name'] = document_name

        headers = self._get_request_headers()
        response = requests.post(DOCUMENTS_URL, data=json.dumps(data), headers=headers)
        try:
            self.document = Document(response.json())
            return self.document
        except:
            raise

    def send_sign_request(self, document='self', from_email=None, message=None, signers=[]):
        '''
        curl -X POST -H 'Authorization: Token api_token'
        -H 'Content-Type:application/json'
        -d '{"document": "https://signrequest.com/api/v1/documents/38595b6b-fdea-45d4-8279-f46e3ae2accd/", "from_email": "ivan@britecore.com", "message": "Please sign this document.\n\nThanks!", "signers": [{"email": "ivan@britecore.com"}]}'
        https://signrequest.com/api/v1/signrequests/
        '''
        # document='self' is a keyword for using same document created before using this instance
        if self.document and document != 'self':
            pass  # Use self document
        else:
            pass  # Use document originally passed arg


class Document:

    def __init__(self, api_response):
        self.url = api_response.get('url')
        self.uuid = api_response.get('uuid')
        self.external_id = api_response.get('external_id')
        self.file_as_pdf = api_response.get('file_as_pdf')
        self.name = api_response.get('name')
        self.pdf = api_response.get('pdf')
        self.security_hash = api_response.get('security_hash')
        self.signrequest = api_response.get('signrequest')
        self.status = api_response.get('status')
        self.file_url = api_response.get('file_url')
        self.file = api_response.get('file')
