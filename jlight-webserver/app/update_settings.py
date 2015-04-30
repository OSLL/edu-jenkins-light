from xmltodict import parse, unparse
from config import SETTINGS_FILE


def save_settings(form):
    settings = {
        u'jenkins_server': {
            u'server_protocol':     form.server_protocol.data,
            u'server_ipaddress':    form.server_ipaddress.data,
            u'server_port':         form.server_port.data,
            u'project_name':        form.project_name.data,
            u'username':            form.username.data,
            u'password':            form.password.data
            }
        }
    settings_data = unparse(settings)

    file = open(SETTINGS_FILE, u'w')
    file.write(settings_data)
    file.close()


def load_settings(form):
    settings = {
        u'server_protocol':     u'http://',
        u'server_ipaddress':    u'127.0.0.1',
        u'server_port':         u'80',
        u'project_name':        u'my_project',
        }

    with (open(SETTINGS_FILE, u'r')) as file:
        settings_data = file.read()
        settings = parse(settings_data)[u'jenkins_server']

    form.server_protocol.process_data(settings[u'server_protocol'])
    form.server_ipaddress.process_data(settings[u'server_ipaddress'])
    form.server_port.process_data(settings[u'server_port'])
    form.project_name.process_data(settings[u'project_name'])
    form.username.process_data(u'')
    form.password.process_data(u'')
