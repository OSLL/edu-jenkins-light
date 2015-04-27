from flask import render_template, flash, redirect
from app import app 
from app.forms import ConfigurateForm

@app.route('/')
@app.route('/status')
def get_status():
    return render_template('status.html',
        title = 'Status')

@app.route('/configurate', methods = ['GET', 'POST'])
def config_server():
    form = ConfigurateForm()
    return render_template('configurate.html', 
        title = 'Configurate',
        form = form)
