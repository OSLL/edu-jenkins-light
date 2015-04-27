from xmltodict import parse, unparse
from config import SETTINGS_FILE


def save_settings(form):
    settings = {
        'jenkins_server': {
            'server_protocol': form.server_protocol.data,
            'server_ipaddress': form.server_ipaddress.data,
            'server_port': form.server_port.data,
            'project_name': form.project_name.data,
            'username': form.username.data,
            'password': form.password.data
            }
        }
    settings_data = unparse(settings)

    file = open(SETTINGS_FILE, 'w')
    file.write(settings_data)
    file.close()


def load_settings(form):
    settings = {
        'server_protocol': 'http://',
        'server_ipaddress': '127.0.0.1',
        'server_port': '80',
        'project_name': 'my_project'
        }

    with (open(SETTINGS_FILE, "r")) as file:
        settings_data = file.read()
        settings = parse(settings_data)['jenkins_server']

    form.server_protocol.data = settings['server_protocol']
    form.server_ipaddress.data = settings['server_ipaddress']
    form.server_port.data = settings['server_port']
    form.project_name.data = settings['project_name']
    form.username.data = "None"
    form.password.data = "None"
