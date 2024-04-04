#!/usr/bin/env python3

import ipdb

class MyString:
    def __init__(self, value='') -> None:
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print('The value must be a string.')

    def is_sentence(self):
        return True if self._value[-1] == '.' else False
    
    def is_question(self):
        return True if self._value[-1] == '?' else False
    
    def is_exclamation(self):
        return True if self._value[-1] == '!' else False
    
    def count_sentences(self):
        split_string = self._value.replace('?', '.').replace('!', '.').split('.')
        return len([s for s in split_string if s])

# simple_string = MyString("one. two. three?")
# empty_string = MyString()
# complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

# print(simple_string.count_sentences())
# print(empty_string.count_sentences())
# print(complex_string.count_sentences())

