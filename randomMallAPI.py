from .util import *
from random import choices
from requests import Session

class randomMallAPI:
    def __init__(self):
        self.api = 'https://randomall.ru/api/{}'.format
        self.session = Session()
        self.headers = headers.Headers().headers
        self.d = ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))

    def fantasyName(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/fantasy_name'), headers = self.headers, json = data)
        return req.json()

    #var is the floor. 1 - male 0 - female
    def appearance(self, var : str) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/appearance'), headers = self.headers, json = data)
        return req.json()

    def crowd(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/crowd'), headers = self.headers, json = data)
        return req.json()

    def character(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/character'), headers = self.headers, json = data)
        return req.json()

    def abilities(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/abilities'), headers = self.headers, json = data)
        return req.json()

    def features(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/features'), headers = self.headers, json = data)
        return req.json()

    def jobs(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/jobs'), headers = self.headers, json = data)
        return req.json()

    def race(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/race'), headers = self.headers, json = data)
        return req.json()

    def superpowers(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/superpowers'), headers = self.headers, json = data)
        return req.json()

    def plot(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/plot'), headers = self.headers, json = data)
        return req.json()

    def plotkeys(self, choice) -> str:
        data = {'choice': choice}
        req = self.session.get(url=self.api('general/plotkeys'), headers = self.headers, json = data)
        return objects.Plotkeys(req.json()).Plotkeys

    def awkwardMoment(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/awkward_moment'), headers=self.headers, json=data)
        return req.json()

    def unexpectedEvent(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/unexpected_event'), headers=self.headers, json=data)
        return req.json()

    def bookName(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/bookname'), headers=self.headers, json=data)
        return req.json()

    def fantasyCountry(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/bookname'), headers=self.headers, json=data)
        return req.json()

    def fantasyTown(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/fantasy_town'), headers=self.headers, json=data)
        return req.json()

    def fantasyContinent(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/fantasy_town'), headers=self.headers, json=data)
        return req.json()

    def countryDescription(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url=self.api('general/country_description'), headers=self.headers, json=data)
        return req.json()

    #repeat : true or false
    def numbers(self, count : str, max : str, min : str, repeat : str) -> str:
        data = {'count': count, 'max': max, 'min': min, 'repeat': repeat, 'symbol': " "}
        req = self.session.post(url = self.api('general/numbers'), headers = self.headers, json = data)
        return req.json()

    #1 - Male, 2 - woman
    def names(self, sex : int) -> str:
        data = {'sex' : sex}
        req = self.session.post(url = self.api('general/names'), headers = self.headers, json = data)
        return req.json()

    def surnames(self):
        req = self.session.post(url = self.api('general/surnames'), headers = self.headers, json = data)
        return req.json()

    #YYYY-MM-DD
    def date(self, start : str, end : str) -> str:
        data = {'start': start, 'end': end}
        req = self.session.post(url = self.api('general/date'), headers = self.headers, json = data)
        return req.json()

    #HH:MM
    def time(self, end : str, start : str) -> str:
        data = {'end': end, 'start': start}
        req = self.session.post(url = self.api('general/time'), headers = self.headers, json = data)
        return req.json()

    def countries(self):
        req = self.session.post(url=self.api('general/countries'), headers=self.headers)
        return req.json()

    def cities(self):
        req = self.session.post(url=self.api('general/cities'), headers=self.headers)
        return req.json()

    def suggestions(self):
        req = self.session.get(url = self.api('gens/suggestions'), headers = self.headers)
        return objects.Suggestions(req.json()).Suggestions

    def gensGenerate(self, id : str) -> str:
        req = self.session.post(url = self.api(f'gens/{id}'), headers = self.headers)
        return req.json()