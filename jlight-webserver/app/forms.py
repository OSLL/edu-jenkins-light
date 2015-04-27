from flask.ext.wtf import Form
from wtforms import TextField, IntegerField
from wtforms.validators import Required
from wtforms.validators import IPAddress
from wtforms.validators import NumberRange


class ConfigurateForm(Form):
    server_protocol = TextField('server_protocol', validators=[Required()])
    server_ipaddress = TextField('server_ipaddress', validators=[IPAddress()])
    server_port = IntegerField('server_port', validators=[NumberRange(min=1, max=65535)])
    project_name = TextField('project_name', validators=[Required()])
    username = TextField('username', validators=[Required()])
    password = TextField('password', validators=[Required()])
