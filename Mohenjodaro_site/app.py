from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/artifacts')
def artifacts():
    return render_template('artifacts.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)



