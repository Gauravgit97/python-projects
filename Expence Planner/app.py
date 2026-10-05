from flask import Flask, render_template, request, url_for, redirect
from expenceTracker import bills_membership


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bills',method=['GET','POST'])
def bills():
    if request.method == 'POST':
        pass
    records = bills_membership.get_records()
    return render_template('bills.html',records=records)



if __name__ == '__main__':
    app.run(debug=True)