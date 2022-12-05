from random import choices
from fake_useragent import FakeUserAgent
from requests import Session

class randomMall:
    def __init__(self):
        self.api = 'https://randomall.ru/api/general/{}'.format
        self.session = Session()
        self.headers = {'user-agent': FakeUserAgent().random}

    def fantasyName(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('fantasy_name'), headers=self.headers, json=data)
        return req.json()

    #var is the floor. 1 - male 0 - female
    def appearance(self, var : str):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31)), 'var': var}
        req = self.session.post(url = self.api('appearance'), headers = self.headers, json=data)
        return req.json()

    def crowd(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('crowd'), headers=self.headers, json=data)
        return req.json()

    def character(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('character'), headers=self.headers, json=data)
        return req.json()

    def abilities(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('abilities'), headers=self.headers, json=data)
        return req.json()

    def features(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('features'), headers=self.headers, json=data)
        return req.json()

    def jobs(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('jobs'), headers=self.headers, json=data)
        return req.json()

    def race(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('race'), headers=self.headers, json=data)
        return req.json()

    def superpowers(self):
        data = {'d': ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=31))}
        req = self.session.post(url=self.api('superpowers'), headers=self.headers, json=data)
        return req.json()