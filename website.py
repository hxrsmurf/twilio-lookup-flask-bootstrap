from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from lookup import number_lookup
app = Flask(__name__)
Bootstrap(app)

result = None

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
  result = number_lookup(request.form['number'])
  return render_template('index.html', lookup_result = result)

if __name__ == '__main__':
    app.run(debug=True)