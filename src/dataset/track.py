import json

class Track :
    def __init__(self, trackpath, jsonpath) -> None:
        self.trackpath = trackpath
        self.jsonpath = jsonpath

    def info(self) -> str:
        return 'track: %s, json: %s' %(self.trackpath, self.jsonpath)
    
    def __str__(self) -> str:
        return 'track: %s, json: %s' %(self.trackpath, self.jsonpath)

    def get_track_path(self):
        return self.trackpath

    def get_json_path(self):
        return self.jsonpath
    
    def read_json(self):
        with open(self.jsonpath, 'r') as read_file:
            return json.load(read_file)