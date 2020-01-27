
#########################################
# Summary
#########################################


@timer
def classify(text):
    query = QueryFactory(text)

    pipeline = Pipeline()
        .naive_bayes_classifier(query.typo_corrected)
        .string_similarity_classifier(query.sanitized)
        .naive_bayes_classifier(query.named_entities_substituted)
        .rnn_classifier(query.sanitized)

    return pipeline.first_with_probability_above(.80)

