from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import *

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Hello This is a webpage for Assignment #4 made by SJ & Mark!'

@app.route('/mbta/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':    #when the user request 'post':
        place_name = str(request.form['a'])   #the input value is accepted as place_name;
        result = find_stop_near(place_name)   #place_name is used as an argument for func 'find_stop_near' from mbta_helper.py
        if result:
            return render_template('mbta_result.html', a=place_name, result=result)  #leads to the mbta_result.html page
    return render_template('mbta_form.html')

if __name__ == '__main__':
    app.run()
