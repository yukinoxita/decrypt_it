import base64

def get_base(s,key):
    if key == 64:
        ans = base64.b64decode(s.encode('utf-8')).decode('utf-8')
    if key == 32:
        ans = base64.b32decode(s.encode('utf-8')).decode('utf-8')
    if key == 16:
        ans = base64.b16decode(s.encode('utf-8')).decode('utf-8')
    return ans
