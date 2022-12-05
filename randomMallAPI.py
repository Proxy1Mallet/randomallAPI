from .util import *
from random import choices
from requests import Session

class randomMallAPI:
    def __init__(self):
        self.api = 'https://randomall.ru/api/{}'.format
        self.session = Session()
        self.headers = headers.Headers().headers
        self.d = ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))

    def fantasyName(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/fantasy_name'), headers = self.headers, json = data)
        return req.json()

    #var is the floor. 1 - male 0 - female
    def appearance(self, var : str):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/appearance'), headers = self.headers, json = data)
        return req.json()

    def crowd(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/crowd'), headers = self.headers, json = data)
        return req.json()

    def character(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/character'), headers = self.headers, json = data)
        return req.json()

    def abilities(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/abilities'), headers = self.headers, json = data)
        return req.json()

    def features(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/features'), headers = self.headers, json = data)
        return req.json()

    def jobs(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/jobs'), headers = self.headers, json = data)
        return req.json()

    def race(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/race'), headers = self.headers, json = data)
        return req.json()

    def superpowers(self):
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/superpowers'), headers = self.headers, json = data)
        return req.json()

    def suggestions(self):
        req = self.session.get(url = self.api('gens/suggestions'), headers = self.headers)
        return objects.Suggestions(req.json()).Suggestions

    def gensGenerate(self, id):
        req = self.session.post(url = self.api(f'gens/{id}'), headers = self.headers)
        return req