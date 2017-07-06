import requests,json

text = requests.post("http://%s:%s/" % ('118.187.53.58', '5500'), json={'a':1,'b':2},headers = {'content-type':
'application/json'})
ret = text.text
print (ret,type(ret))