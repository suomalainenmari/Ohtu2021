import toml
from urllib import request
from project import Project



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)
        wanteddata = (parsed_toml["tool"]["poetry"])
        #print(tool)

        return Project(wanteddata["name"], wanteddata["description"], wanteddata["dependencies"], wanteddata["dev-dependencies"])
        #return Project("Test name", "Test description", [], [])
