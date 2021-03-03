import flask
from flask import request, jsonify
import data


app = flask.Flask(__name__)
app.config['Debug'] = False


@app.route('/hpscholar', methods=['GET'])
def api_all():
    if 'title' in request.args:
        title = request.args['title']
        pubJSON = data.fetchPublication(title)
        resp = flask.Response(pubJSON)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    else:
        return flask.Response('No Record Found') 
     
app.run()    