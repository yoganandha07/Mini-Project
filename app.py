from flask import Flask, request, render_template, redirect, url_for, flash, session
import numpy as np
import pickle

model = pickle.load(open('data/model.pkl', 'rb'))

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session management

# Simulated user database
users = {
    'Yoganandha': '5139',
    'Vishnu': 'Vardhan98',
    'Bhrami': 'Bhrami12'
}

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template("index.html", username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials, please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    input_features = request.form.getlist('features')
    
    cleaned_features = []
    for feature in input_features:
        cleaned_feature = ''.join(c for c in feature if c.isdigit() or c == '.')
        cleaned_features.append(cleaned_feature)
    
    input_features = np.array(cleaned_features, dtype=float).reshape(1, -1)
    
    prediction = model.predict(input_features)[0]

    
    return render_template('index.html', prediction_text=f'Predicted Sales: {prediction}', username=session.get('username'))

if __name__ == '__main__':
    app.run()