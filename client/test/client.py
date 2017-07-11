import requests,json
a = ['gggddd','hhhh']
text = requests.post("http://%s:%s/post"%('127.0.0.1','9000'),json=a,headers = {'content-type':'application/json'},timeout = 600)
print (text.status_code,'*******服务器返回码')
if text.status_code == 200:
    print (json.loads(text.text))