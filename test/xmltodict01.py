import xmltodict
from pprint import pprint 



settings_file = "settings.xml"


with (open (settings_file, "r")) as file:
    settings_data = file.read ()

settings = xmltodict.parse (settings_data) ["jenkins_server"]

pprint (settings)