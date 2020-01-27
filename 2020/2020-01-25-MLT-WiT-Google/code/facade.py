#########################################
# Facade
#########################################


s3.write('some_s3_bucket', 'corpora/1234/corpus.json', corpus)
s3.write('some_s3_bucket', 'models/classifier_1234.gz',
        gzip(pickle.dump(classifier)))
db.insert('database1', 'current_model_id', 1234)
...

model_id = db.get('database1', 'current_model_id')
corpus = json.loads(s3.read('some_s3_bucket',
    'corpora/{}/corpus.json'.format(model_id)))
classifier = pickle.loads(gunzip(s3.read('some_s3_bucket'),
        'models/classifier_{}}.gz'.format(model_id)))
...
prediction = classifier.classify('foo')



data_facade = DataFacade(1234)

data_facade.put_corpus(corpus)
data_facade.put_classifier(corpus)
data_facade.put_current_model_id()
...
model_id = data_facade.get_current_model_id()
corpus = data_facade.get_corpus()
classifier = data_facade.get_classifier()



class DataFacade:

    S3_BUCKET = 'some_s3_bucket'
    DATABASE = 'database1'

    def __init__(self, model_id):
        self.model_id = model_id

    def get_corpus(self):
        return json.loads(s3.read(S3_BUCKET,
            'corpora/{}/corpus.json'.format(self.model_id)))

    def put_corpus(self, corpus):
        s3.write(S3_BUCKET, 'corpora/{}/corpus.json'
            .format(self.model_id), corpus)

    def get_current_model_id(self):
        return db.get(DATABASE, 'current_model_id')

    def put_current_model_id(self):
        db.insert(DATABASE, 'current_model_id', self.model_id)

    def get_classifier(self):
        return pickle.loads(gunzip(s3.read(S3_BUCKET),
                'models/classifier_{}}.gz'.format(self.model_id)))

    def put_classifier(self, classifier):
        s3.write(S3_BUCKET, 'models/classifier_{}.gz'.format(self.model_id),
                gzip(pickle.dump(classifier)))
