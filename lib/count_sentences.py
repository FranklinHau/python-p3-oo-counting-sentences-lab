#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=''):
    self._value = None 
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, val):
    if not isinstance(val, str):
      print('The value must be a string.')
    else:
      self._value = val

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False 
  
  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
    sentences = re.split(r'[.!?]', self.value)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)
    
  value=property(get_value, set_value)


my_string = MyString()
my_string.value = 'Hello, world!'
print(my_string.is_sentence())
my_string.value = 'Hello, word.'
print(my_string.is_sentence())
my_string.value = 'Why?'
print(my_string.is_question())
my_string.value = "Hello, world! How are you? I'm fine."
print(my_string.count_sentences())
