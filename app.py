from flask import Flask, render_template, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data', methods=['GET'])
def get_data():
    try:
        conn_data = pd.read_csv('conn_raw.csv')
        logs = []
        with open('decision.log', 'r') as log_file:
            logs = log_file.readlines()
        
        conn_list = conn_data.to_dict(orient='records')

        return jsonify({
            'conns': conn_list,
            'logs': logs
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })

@app.route('/retrain', methods=['POST'])
def retrain_model():
    return jsonify({'status': 'Modelo reentrenado exitosamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
