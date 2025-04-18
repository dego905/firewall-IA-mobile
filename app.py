from flask import Flask, render_template, jsonify, request import pandas as pd import os

app = Flask(name)

@app.route('/') def dashboard(): return render_template('dashboard.html')

@app.route('/data') def data(): log_path = 'decision.log' conn_path = 'conn_raw.csv' logs = [] conns = []

if os.path.exists(log_path):
    with open(log_path, 'r') as f:
        logs = f.readlines()

if os.path.exists(conn_path):
    try:
        df = pd.read_csv(conn_path)
        conns = df.to_dict(orient='records')
    except:
        conns = []

return jsonify({
    'logs': logs[-20:],
    'conns': conns[-20:]
})

@app.route('/retrain', methods=['POST']) def retrain(): os.system('python ai_detect.py --retrain') return jsonify({'status': 'Modelo reentrenado'})

if name == 'main': app.run(debug=True, host='0.0.0.0')

