from flask import Flask, request, Response, render_template # pip install Flask
import json

app = Flask(__name__)

positions = [[51.5, -0.09], [51.6, -0.10], [51.7, -0.11]]

@app.route('/')
def home():
    return render_template('maptest.html')

@app.route('/api/positions')
def get_positions():
    # sarjallistetaan measurements-lista json-muotoon
    s = json.dumps(positions, indent=True)
    # tehdään vastaus oikealla tavalla
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)    

if __name__ == '__main__':
    app.run(debug=True)