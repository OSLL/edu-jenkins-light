from flask import render_template, flash, redirect
from app import app
from app.forms import ConfigurateForm
from app.update_settings import save_settings, load_settings


@app.route('/')
@app.route('/status')
def get_status():
    return render_template(
        'status.html',
        title='Status')


@app.route('/configurate', methods=['GET', 'POST'])
def config_server():
    form = ConfigurateForm()

    if form.validate_on_submit():
        save_settings(form)
        return redirect('/')

    load_settings(form)
    return render_template(
        'configurate.html',
        title='Configurate',
        form=form)
