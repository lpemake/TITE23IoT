from flask import Flask, request, Response, render_template # pip install Flask
import json

app = Flask(__name__)

measurements = []

# näytetään HTML-sivu, jossa on google chart
@app.route('/line')
def show_line():
    return render_template('linechart.html')

# näytetään HTML-sivu, jossa on pie chart
@app.route('/pie')
def show_pie():
    return render_template('pie.html')

# näytetään data HTML-sivulla
@app.route('/')
def show_test():
    return render_template('testi.html')

@app.route('/api/distribution')
def distribution():
    dist = []
    dist.append(['>4', 0])
    dist.append(['0...4', 0])
    dist.append(['-4...0', 0])
    dist.append(['<-4', 0])
    for row in measurements:
        lampotila = row['field2']
        if lampotila < -4:
            dist[3][1] += 1
        elif lampotila < 0:
            dist[2][1] += 1
        elif lampotila < 4:
            dist[1][1] += 1
        else:
            dist[0][1] += 1
    # muutetaan json-muotoon
    s = json.dumps(dist)
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)

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
    # lisätään mittaus listan alkuun
    # measurements.append(meas)
    measurements.insert(0, meas)
    meas_json = json.dumps(meas)
    # palautetaan lisätty mittaus asiakkaalle
    # (REST API haluaa näin)
    return meas_json

if __name__ == '__main__':
    app.run(debug=True)

