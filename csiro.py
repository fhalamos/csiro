from flask import Flask, redirect
from flask.json import jsonify
app = Flask(__name__)

cache = {}
cache['foo'] = 1

@app.route('/')
def start(): 
    if cache['foo']==1:
    	cache['foo']=2
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeoBILwagcyCB6mewN0k0Ss9VSfjYRWfyhZpgleEhufPI8Ryg/viewform", code=302)
    elif cache['foo']==2:
    	cache['foo']=3
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeN-0nIRL-EwJUtVyO23fXbcInqN3Z2PAf4hAYFIEsAWBYeJQ/viewform", code=302)
    elif cache['foo']==3:
    	cache['foo']=4
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc43vtJYsv12JrfPh4tu6Qtzmqxb2aa1DMLcysZjq2bAerVCg/viewform", code=302)
    elif cache['foo']==4:
    	cache['foo']=1
    	return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfbmEe-7eBfuQN_DL2HiWOxR_WCCvGjJrGQNARKLpcVA9zWTQ/viewform", code=302)    	




if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')

