#########################################
# Dependency injection
#########################################

class Algorithm():

    def predict(self):
        data_facade = DataFacade()
        data_facade.get_corpus(corpus) # Calls S3
        ...

class Algorithm():

    def predict(self, _data_facade = None):
        data_facade = _data_facade or DataFacade()
        data_facade.get_corpus(corpus)
        ...

class Algorithm():

    def __init__(self, _data_facade = None):
        self.data_facade = _data_facade or DataFacade()

    def predict(self):
        self.data_facade.get_corpus(corpus)
        ...



def test_predict_with_simple_corpus(self):
    # GIVEN
    # configure mocks
    mock_data_facade = unittest.mock.create_autospec(DataFacade)
    mock_data_facade.get_corpus.return_value = Corpus(['foo'])

    algo = Algorithm(_data_facade=mock_data_facade) # inject

    # WHEN
    result = algo.predict()

    # THEN
    self.assertEqual(result, 'foo', ...)
