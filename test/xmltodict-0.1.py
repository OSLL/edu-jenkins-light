from xmltodict import parse, unparse
from pprint import pprint


settings_file = 'settings.xml'

with (open(settings_file, 'r')) as file:
    settings_data = file.read()

settings = parse(settings_data)
pprint(settings)


settings_data = unparse(settings)
file = open(settings_file, 'w')
file.write(settings_data)
