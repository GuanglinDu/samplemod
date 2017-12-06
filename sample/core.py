# -*- coding: utf-8 -*-
from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

def add(a, b):
    return a + b;


class Addition(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
