from flask import render_template, redirect
from app import app
from app.forms import ConfigurateForm
from app.update_settings import save_settings, load_settings
from config import PROJECT_STATUS_DATA_FILE as statusPath


@app.route('/')
@app.route('/status')
def get_status():
    with (open(statusPath, 'r')) as file:
        status = file.read()

    return render_template(
        'status.html',
        title='Status', status=status)


@app.route('/configurate', methods=['GET', 'POST'])
def config_server():
    form = ConfigurateForm()

    if (form.is_submitted() and
            form.load_settings.data):
        load_settings(form)
    elif (form.is_submitted() and
            form.submit.data and
            form.validate()):
        save_settings(form)
        return redirect('/')

    return render_template(
        'configurate.html',
        title='Configurate',
        form=form)
