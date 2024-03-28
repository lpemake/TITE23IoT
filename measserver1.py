from flask import Flask, request, Response, render_template # pip install Flask
import json

app = Flask(__name__)

measurements = []

# näytetään HTML-sivu, jossa on google chart
@app.route('/line')
def show_line():
    return render_template('linechart.html')

# näytetään data HTML-sivulla
@app.route('/')
def show_test():
    return render_template('testi.html')

# palautetaan mittaukset json-muodossa
@app.route('/api/meas2')
def showmeas2():
    # sarjallistetaan measurements-lista json-muotoon
    chartmeas = []

    aika = 0
    # muutetaan sanakirjat listaksi
    for row in measurements:
        chartrow = []
        chartrow.append(aika) # aika
        chartrow.append(row["field1"])
        chartrow.append(row["field2"])
        chartrow.append(row["field3"])
        # lisätään uusi rivi päälistaan
        chartmeas.append(chartrow)
        aika += 1

    s = json.dumps(chartmeas, indent=True)
    # tehdään vastaus oikealla tavalla
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)

# palautetaan mittaukset json-muodossa
@app.route('/api/meas')
def showmeas():
    # sarjallistetaan measurements-lista json-muotoon
    s = json.dumps(measurements, indent=True)
    # tehdään vastaus oikealla tavalla
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)

# mittausten vastaanotto
@app.route('/newmeas', methods = ['POST'])
def newmeas():
    # poimitaan mittaus HTTP POST -viestistä
    meas = request.get_json()
    # lisätään mittaus listaan
    measurements.append(meas)
    meas_json = json.dumps(meas)
    # palautetaan lisätty mittaus asiakkaalle
    # (REST API haluaa näin)
    return meas_json

if __name__ == '__main__':
    app.run(debug=True)

