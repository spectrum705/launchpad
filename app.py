from flask import Flask, abort, request, json
from flask import jsonify
import requests
import os

#create flask app
# API_KEY = os.environ['API_KEY']
# API_KEY =

app=Flask(__name__)


@app.route('/')
def home():
    try:
        url='https://ll.thespacedevs.com/2.2.0/launch/?format=json'
        request_data= requests.get(url)
        request_data=request_data.json()
        launch=request_data['results']
        return jsonify(launch), 200
    except:
        return jsonify({'error':'An error occured'}), 400



		# specific launchpad, second endpoint
@app.route('/<id>')
def one_launch(id):
    try:
        url=f'https://ll.thespacedevs.com/2.2.0/launch/{id}/?format=json'
        request_data= requests.get(url)
        request_data=request_data.json()    
        
        return jsonify(request_data), 200
    except:
        return jsonify({'error':'An error occured'}), 400
    
    
if __name__ == '__main__':
    app.run(debug=True)
    