from flask import Flask, redirect, url_for, request ,render_template
from reviewanalysis import *
from datafeed import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/thanks')
def thanks():
   return render_template('ThankYou.html')

@app.route('/sucess/<name>/<rating>/<review>')
def success(name,rating,review):
    reviewrate=output_scenti(review)
    appendexcel(name,rating,review,reviewrate)
    return redirect(url_for('thanks'))

@app.route('/feedbackform', methods=['POST'])
def feedbackform():
    if request.method == 'POST':
        cname = request.form.get("cuname",None)
        ctext = request.form.get("cure",None)
        crating = request.form.get("rate",None)
        return redirect(url_for('success', name=cname,rating=crating,review=ctext))
if __name__ == '__main__':
    app.run(debug=True)