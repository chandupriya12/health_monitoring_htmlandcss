from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory storage for simplicity (use a database for a real application)
health_data = []

@app.route('/')
def index():
    return render_template('index.html', health_data=health_data)

@app.route('/add', methods=['POST'])
def add_health_data():
    data = {
        'date': request.form['date'],
        'weight': request.form['weight'],
        'blood_pressure': request.form['blood_pressure'],
        'heart_rate': request.form['heart_rate']
    }
    health_data.append(data)
    return redirect(url_for('index'))

@app.route('/api/data', methods=['GET'])
def get_health_data():
    return jsonify(health_data)

if __name__ == '__main__':
    app.run(debug=True)
