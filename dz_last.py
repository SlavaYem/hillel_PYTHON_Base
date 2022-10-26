import json
import requests


def sort_surname(item):
    my_name = item['quoteAuthor']
    my_sort_name = my_name.split()[-1]
    return my_sort_name


class Quotes:
    def __init__(self, qoutes: int, filename: str):
        self.filename = filename
        self.qoutes = qoutes

    def get_qoutes(self):
        my_list = []
        url = "http://api.forismatic.com/api/1.0/"
        for key in range(self.qoutes):
            params = {
                "method": "getQuote",
                "format": "json",
                "key": key,
                "lang": "en"
            }
            response = requests.get(url, params=params)
            try:
                my_new_response = response.json()

            except json.decoder.JSONDecodeError:
                print("ERROR")

            if not my_new_response['quoteAuthor']:
                my_list = []
            else:
                my_list.append(my_new_response)
        return my_list

    def print_qoutes(self):
        my_list = self.get_qoutes()
        for index in range(len(my_list)):
            print(f"Qoutes: {my_list[index]['quoteText']} Avtor: {my_list[index]['quoteAuthor']}")

    def save_qoutes_in_json(self):
        with open(self.filename, "w") as json_file:
            my_list = self.get_qoutes()
            my_sorted_list = sorted(my_list, key=sort_surname)
            json.dump(my_sorted_list, json_file, indent=4)
        return my_list


qoutes = 10
filename = "data1.json"
first = Quotes(qoutes, filename)
first.save_qoutes_in_json()
first.print_qoutes()
