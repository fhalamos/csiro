from flask import Flask, redirect
from flask.json import jsonify

import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

cache = {}
cache['foo'] = 1
respForm1="Sistema de evaluacion de riesgo (1) (Responses)"
respForm2="Sistema de evaluacion de riesgos (2) (Responses)"
linkForm1 = "https://docs.google.com/forms/d/e/1FAIpQLScm2UtvEWgHYjXD5C1JvgSdbem-n3K6E6CYC4vE4Yzu1DXWSw/viewform"
linkForm2 = "https://docs.google.com/forms/d/e/1FAIpQLSfaY3VHOQdZhi09ejcvCb0YbKzHKQptYSWf3Sd4WiQW_Mq5gw/viewform"


scope=""
creds=""
client=""
sheet=""

def iniciarSesionSheets():
	# use creds to create a client to interact with the Google Drive API
	global scope
	global creds
	global client

	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
	 
	


def cantRespuestas(linkRespForm):
	global sheet
	sheet = client.open(linkRespForm).sheet1

	primera_columna = sheet.col_values(1)
	primera_columna.pop(0)
	contador=0

	for fila in primera_columna:
		if fila != "":
			contador = contador+1

	print (contador)
	return contador



@app.route('/')
def start(): 
	iniciarSesionSheets()
	if cantRespuestas(respForm1)>cantRespuestas(respForm2):
		return redirect(linkForm2, code=302)
	else:
		return redirect(linkForm1, code=302)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')

