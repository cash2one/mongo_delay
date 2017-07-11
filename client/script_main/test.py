import base64
a = 'ggggg'
tmp = base64.b64encode(bytes(a,encoding='utf-8'))


tmp = str(base64.b64decode(tmp),encoding='utf8')
print (tmp)
