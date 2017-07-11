import json
from flask import Flask,request,Response
app = Flask(__name__)

@app.route('/get', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()  # {'type':'get/send','content':''} type代表抓取器的请求类型，get为得到抓取任务，post是上传解析任务。task为具体的上传任务
        print (message)
        result = 'get'
        return Response(json.dumps(result), mimetype='application/json')

@app.route('/post', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        message = request.get_json()  # {'type':'get/send','content':''} type代表抓取器的请求类型，get为得到抓取任务，post是上传解析任务。task为具体的上传任务
        print (message)
        result = 'post'
        return Response(json.dumps(result), mimetype='application/json')



def run():
    app.run(host='127.0.0.1', port=9000)#抓取器访问的本地地址.

run()