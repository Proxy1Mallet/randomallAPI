class Suggestions:
    def __init__(self, data):
        self.json = data
        self.suggestions0 = None
        self.suggestions1 = None
        self.suggestions2 = None
        self.suggestions3 = None
        self.suggestions4 = None
        self.suggestions5 = None
        self.suggestions6 = None
        self.suggestions7 = None

    @property
    def Suggestions(self):
        self.suggestions0 = self.json[0]
        self.suggestions1 = self.json[1]
        self.suggestions2 = self.json[2]
        self.suggestions3 = self.json[3]
        self.suggestions5 = self.json[4]
        self.suggestions5 = self.json[5]
        self.suggestions6 = self.json[6]
        self.suggestions7 = self.json[7]
        return self

class Plotkeys:
    def __init__(self, data):
        self.json = data
        self.category = None
        self.position = None
        self.name = None
        self.title = None
        self.descriptionMainpage = None
        self.descriptionGenerator = None
        self.metaDescription = None
        self.metaKeywords = None
        self.usergen = None

    @property
    def Plotkeys(self):
        self.category = self.json['category']
        self.position = self.json['position']
        self.name = self.json['name']
        self.title = self.json['title']
        self.descriptionMainpage = self.json['descriptionMainpage']
        self.descriptionGenerator = self.json['descriptionGenerator']
        self.metaDescription = self.json['metaDescription']
        self.metaKeywords = self.json['metaKeywords']
        self.usergen = self.usergen['usergen']
        return self