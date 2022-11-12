from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response
import random
import Files.delzone as dz
import pandas as pd
app = Flask(__name__)
# logged_in = False
@app.route('/', methods=['GET', 'POST'])

def index():
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                   resp = make_response(render_template('dashboard.html'))
                   global cookie
                   cookie = random.randint(1, 100000)
                   resp.set_cookie('uid', )
                   return resp
        return render_template('index.html')


@app.route('/dashboard')

def dashboard():
    uid = request.cookies.get('uid')
    try:
        if uid == cookie:
            Zone1 = dz.readZones('1', 'num')
            Zone2 = dz.readZones('2', 'num')
            Zone3 = dz.readZones('3', 'num')
            Zone4 = dz.readZones('4', 'num')
            Zone5 = dz.readZones('5', 'num')
            # print(Zone1, Zone2, Zone3, Zone4, Zone5)
            return render_template('dashboard.html', value=Zone1+","+Zone2+","+Zone3+","+Zone4+","+Zone5)
        else:
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))

@app.route('/list')

def list():
    # uid = request.cookies.get('uid')
    # try:
    #     if uid == cookie:
    data = pd.read_csv('Files/zone.txt', sep=';')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
    #     else:
    #         return redirect(url_for('index'))
    # except:
    #     return redirect(url_for('index'))
    # converting csv to html
    
@app.route('/add', methods=['GET', 'POST'])

def add():
    if request.method == 'POST':
        name = request.form['name']
        zip = request.form['zip']
        zone = request.form['zone']
        if dz.addSub(name, zip, zone):
            return render_template('dashboard.html')
        else:
            return render_template('dashboard.html')
    else:
        return render_template('add.html')

app.run(host="0.0.0.0", port=8000)