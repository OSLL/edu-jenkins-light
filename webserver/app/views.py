from flask import render_template, redirect
from app import app
from app.forms import ConfigurateForm
from app.update_settings import save_settings, load_settings


@app.route('/')
@app.route('/status')
def get_status():
    data_file = '/home/work/project/proj/status.data'
    
    with (open(data_file, 'r')) as file:
        settings_data = file.read()

    return settings_data
    '''return render_template(
        'status.html',
        title='Status')'''


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
