#########################################
# Adapter
#########################################

{
    'meta': {
        'id': 1234
        'date': '2020/01/25'
    },
    'cases': [
        [
            {
                'text': 'I really like pancakes',
                'source': 'twitter'},
            {
                'value': 'positiveSentiment',
                'labeller': 'Chris'
            },
        ],
        ...
    ]
}

data = json.loads(download_raw_data())

print('Processing ID {}'.format(data['meta']['id']))

inputs = []
labels = []

for item in data['cases']:
    if len(item) > 2:
        if 'text' in item[0] and 'value' in item[1]:
            cleaned_input = clean(item[0]['text'])
            inputs.append(cleaned_input)
            labels.append(item[1]['value'])

model.train(inputs, labels)



data = json.loads(download_raw_data())
corpus = CorpusJsonAdapter(data)

print('Processing ID {}'.format(corpus.id))

model.train(corpus.inputs, corpus.labels)



data = json.loads(download_raw_data())

corpus = Corpus.from_json(data)

print('Processing ID {}'.format(corpus.id))

model.train(corpus.inputs, corpus.labels)



data_obj = RawData(data)
corpus = data_obj.to_corpus()

print('Processing ID {}'.format(corpus.id))

model.train(corpus.inputs, corpus.labels)



class Corpus:

    def __init__(self, id):
        self.id = None
        self.inputs = []
        self.labels = []


class CorpusJsonAdapter(Corpus):

    def __init__(self, data):
        self.id = data['meta']['id']

        for item in data['cases']:
            if len(item) > 2:
                if 'text' in item[0] and 'value' in item[1]:
                    cleaned_input = clean(item[0]['text'])
                    self.inputs.append(cleaned_input)
                    self.labels.append(item[1]['value'])


class Corpus:

    def __init__(self, id):
        self.id = None
        self.inputs = []
        self.labels = []

    @staticmethod
    from_json(data):
        corpus = Corpus()
        corpus.id = data['meta']['id']

        for item in data['cases']:
            if len(item) > 2:
                if 'text' in item[0] and 'value' in item[1]:
                    cleaned_input = clean(item[0]['text'])
                    corpus.inputs.append(cleaned_input)
                    corpus.labels.append(item[1]['value'])



class Corpus:

    def __init__(self, id):
        self.id = id
        self.inputs = []
        self.labels = []


class RawData:

    def __init__(self, data):
        self.meta = RawData.Meta(data['meta'])
        self.cases = [RawData.Case(d) for d in data['cases']]

    class Meta:
        def __init__(self, data):
            self.id = data['id']

    class Case:

        def __init__(self, data):
            self.textinfo = RawData.Case.Text(data[0])
            self.valueinfo = RawData.Case.Value(data[1])

            class Text:
                def __init__(self, data):
                    self.text = data.get('text')
                    self.source = data.get('source') # not used

            class Value:
                def __init__(self, data):
                    self.value = data.get('value')
                    self.labeller = data.get('labeller') # not used

    def to_corpus():
        corpus = Corpus(self.meta.id)

        for case in self.cases:
            if case.textinfo.text and case.valueinfo.value:
                cleaned_input = clean(case.textinfo.text)
                corpus.inputs.append(cleaned_input)
                corpus.labels.append(case.valueinfo.value)
