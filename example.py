from signrequest import SignRequest

API_KEY = '36254658dc554d96a956d34e62e342e0b67e5887'
document = 'https://signrequest.com/api/v1/documents/c27f3e0b-616a-4a74-9182-c00d4e3aa16a/'
sr = SignRequest(API_KEY).send_sign_request(document=document,
                                            from_email='ivan@britecore.com',
                                            message='Please sign this thing.',
                                            signers=['ivanrodriguezo@gmail.com'])

print sr.uuid
