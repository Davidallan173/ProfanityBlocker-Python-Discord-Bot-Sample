import json

class ProfanityConfiguration:
    def __init__(self):
        configFile = open("config.json", "r")
        self.config = json.load(configFile)
        configFile.close()

    def GetConfigVar(self, variable, default=None):
        if variable in self.config.keys():
            return self.config[variable]
        return default