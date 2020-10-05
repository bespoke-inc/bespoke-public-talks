#########################################
# Factory
#########################################

original_text = 'Hello! how are you todya? :)'

res = predict(original_text)
if not res:
    sanitized_text = make_ascii(original_text.lower())
    res = predict(sanitized_text)
if not res:
    res = predict(typo_correct(original_text))
if not res:
    san_and_typo_text = typo_correct(sanitized_text)
    res = predict(san_and_typo_text)

return res


original_text = 'Hello! how are you todya? :)'

text_factory = TextFactory(original_text)

res = predict(original_text)
if not res:
    res = predict(text_factory.sanitized())
if not res:
    res = predict(text_factory.typo_corrected())
if not res:
    res = predict(text_factory.sanitized_and_typo_corrected())

return res


class TextFactory:

    def __init__(self, text):
        self.raw = text

    def sanitized(self):
        if not self._sanitized:
            self._sanitized = make_ascii(self.raw.lower())
        return self._sanitized

    def typo_corrected(self):
        if not self._typo_corrected:
            self._typo_corrected = typo_correct(self.raw)
        return self._typo_corrected

    def sanitized_and_typo_corrected(self):
        if not self._sanitized_and_typo_corrected:
            self._sanitized_and_typo_corrected = typo_correct(self.sanitized())
        return self._sanitized_and_typo_corrected



res = predict(original_text)
if not res:
    sanitized_text = sanitized(original_text) # remove punctuation, etc
    res = predict(sanitized_text)
if not res:
    typo_corrected_text = typo_correct(original_text) # todya => today
    if typo_corrected_text != sanitized_text:
        res = predict(typo_corrected_text)
if not res:
    san_and_typo_text = typo_correct(sanitized_text)
    if san_and_typo_text != sanitized_text and san_and_typo_text != typo_corrected_text:
        res = predict(san_and_typo_text)

return res