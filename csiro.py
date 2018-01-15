from flask import Flask, redirect
from flask.json import jsonify
app = Flask(__name__)

cache = {}
cache['foo'] = 1

@app.route('/')
def start(): 
    if cache['foo']==1:
    	cache['foo']=2
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLScm2UtvEWgHYjXD5C1JvgSdbem-n3K6E6CYC4vE4Yzu1DXWSw/viewform", code=302)
    elif cache['foo']==2:
    	cache['foo']=1
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfaY3VHOQdZhi09ejcvCb0YbKzHKQptYSWf3Sd4WiQW_Mq5gw/viewform", code=302)



if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')

