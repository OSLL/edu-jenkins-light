from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, IPAddress, Optional, ValidationError


class TextNumberRange(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Number must be between %d and %d.' % (min, max)
        self.message = message

    def __call__(self, form, field):
        if (not field.data.isnumeric() or
                int(field.data) < self.min or
                int(field.data) > self.max):
            raise ValidationError(self.message)


class ConfigurateForm(Form):
    server_protocol = TextField(u'server protocol',
                                validators=[Required()])
    server_ipaddress = TextField(u'server ipaddress',
                                 validators=[IPAddress()])
    server_port = TextField(u'server port',
                            validators=[TextNumberRange(min=1, max=65535)])
    project_name = TextField(u'project name',
                             validators=[Required()])
    username = TextField(u'username',
                         validators=[Optional()])
    password = PasswordField(u'password',
                             validators=[Optional()])
    load_settings = SubmitField(u'Load settings')
    submit = SubmitField(u'submit')
