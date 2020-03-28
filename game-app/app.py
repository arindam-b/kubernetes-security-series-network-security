from flask import Flask
import os
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    return "Home page of Football App"


@app.route('/football/<team>', methods=['GET'])
def footballapp(team):
    response = requests.get(url = 'http://game-api:8080/footballwc/'+team)
    print(response)
    return f"{team} has won world cup {response.text}", 200
	
# This is for debug mode on
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
