from flask import render_template, redirect
from app import app
from app.forms import ConfigurateForm
from app.update_settings import save_settings, load_settings


@app.route(u'/')
@app.route(u'/status')
def get_status():
    data_file = '/home/work/project/proj/status.data'
    
    with (open(data_file, 'r')) as file:
        settings_data = file.read()

    return settings_data
    '''return render_template(
        u'status.html',
        title=u'Status')'''


@app.route(u'/configurate', methods=[u'GET', u'POST'])
def config_server():
    form = ConfigurateForm()

    if (form.is_submitted() and
            form.load_settings.data):
        load_settings(form)
    elif (form.is_submitted() and
            form.submit.data and
            form.validate()):
        save_settings(form)
        return redirect(u'/')

    return render_template(
        u'configurate.html',
        title=u'Configurate',
        form=form)
