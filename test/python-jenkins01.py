from jenkins import Jenkins, JenkinsError
import xmltodict 
from pprint import pprint 



#import settings

settings_file = "settings.xml"


with (open (settings_file, "r")) as file:
	settings_data = file.read ()

settings = xmltodict.parse (settings_data) ["jenkins_server"]



#connecting to server and check project status

server = Jenkins (settings ["url"], settings ["username"], settings ["password"])

project_info = server.job_info (settings ["project_name"])

pprint (project_info ['healthReport'])