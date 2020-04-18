import requests
import json
import wikipedia

class SearchLinks:
    def __init__(self, path):
        self.path = path
        self.session = requests.session
        self.idx = -1
        with open(self.path, encoding='utf-8') as inputfile:
            self.data = json.load(inputfile)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == len(self.data):
            raise StopIteration
        country = self.data[self.idx]['name']['common']
        try:
            search = wikipedia.search(country, results=1)
            page = wikipedia.page(search[0])
            url = page.url
            return country, url
        except:
            return country, 'Information not found :('

if __name__=='__main__':
    with open('links.txt', 'w', encoding='utf-8') as outfile:
        for country in SearchLinks('countries.json'):
            outfile.write("{} - {}\n".format(*country))


