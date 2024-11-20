import requests
import json

class apiWaiter:
    """
    Performs interactions and requests data with API Server
    """
    def __init__(self):
        """
        Constructor
        """
        
    def submitToServer():
        """
        Submits url to API server to receive results
        @return: the json results
        """
        
        response = requests.get("https://app.zipcodebase.com/api/v1/code/city?apikey=a0f42fd0-a762-11ef-8709-97910ef36bb5&city=Amsterdam&state_name=Noord-Holland&country=nl&limit=1")

        apiResults = response.content
        
        return apiResults

    def loadJSONtoDict(self, jsonResponse):
        """
        Loads JSON data into a dictionary
        @param jsonResponse: the JSON data
        @return: the dictionary
        """
        parsed_json = json.loads(jsonResponse)

        return parsed_json 