# Credentials For AWS...
# Will need to hide or encode...

import os

AWS_ACCESS_KEY_ID = "AKIA3LFTTMYFP76BGHTB"
AWS_SECRET_ACCESS_KEY = "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"

AWS_ACCESS_KEY_ID_secured = os.environ['AWS_ACCESS_KEY_ID_secured']
AWS_SECRET_ACCESS_KEY_secured = os.environ['AWS_SECRET_ACCESS_KEY_secured']


AWS_REGION = "us-east-1"
DYNAMO_ENABLE_LOCAL = False
DYNAMO_LOCAL_HOST = None
DYNAMO_LOCAL_PORT = None