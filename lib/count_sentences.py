#!/usr/bin/env python
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print('The value must be a string.')

    def get_value(self):
        return self._value

    value = property(get_value, set_value)

    def is_sentence(self):
        return True if self._value.endswith('.') else False

    def is_question(self):
        return True if self._value.endswith('?') else False

    def is_exclamation(self):
        return True if self._value.endswith('!') else False

    def count_sentences(self):
        # Use regular expression to split the string by sentence-ending punctuation marks
        sentences = re.split(r'[.!?]', self._value)
        # Remove empty strings from the list
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(non_empty_sentences)
