
from flask import Flask,request,Response
import json
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        a = request.get_json()
        print (a)
        rt = {'g':1,'h':2}
        return Response(json.dumps(rt), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8989)