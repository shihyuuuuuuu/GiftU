import base64

def encode(x):
    return base64.b64encode(x.encode("utf-8")).decode("utf-8")

def decode(x):
    return base64.b64decode(x.encode("utf-8")).decode("utf-8")
    