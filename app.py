from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    firstname = request.form['name']
    birthdate_str = request.form['date']
    
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        current_year = datetime.now().year
        age = current_year - birthdate.year
        return jsonify({'firstname': firstname, 'age': age})  
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
