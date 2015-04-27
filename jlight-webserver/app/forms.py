from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from wtforms.validators import IPAddress
from wtforms.validators import NumberRange


class ConfigurateForm(Form):
    server_ipadress = TextField('server_ipadress', validators=[IPAddress()])
    server_port = TextField('server_port', validators=[NumberRange(min=1, max=65535)])
    project_name = TextField('project_name', validators=[Required()])
    username = TextField('username')
    password = TextField('password')
