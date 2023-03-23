import json

class JsonReader:
    @staticmethod
    def get_test_data():
        # Opening JSON file
        json_file = open('testdata/data.json')

        # returns JSON object as
        # a dictionary
        data = json.load(json_file)

        # Closing file
        json_file.close()

        # return data
        return data['emp_details']