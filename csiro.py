from flask import Flask, redirect
from flask.json import jsonify
app = Flask(__name__)

cache = {}
cache['foo'] = 1

@app.route('/')
def start(): 
    if cache['foo']==1:
    	cache['foo']=0
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfqHTAOCVUAbW4xEN2dnL_lHjvjtTz5RBclJpHYPi4Wo5TFwg/viewform", code=302)
    elif cache['foo']==0:
    	cache['foo']=1
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeXMowAZqlmandnKxlrGjq5kzNp0sFwFhy9XqlvHvKGGUXPow/viewform", code=302)
 

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')

