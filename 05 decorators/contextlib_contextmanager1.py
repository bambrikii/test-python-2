#!/bin/python

from __future__ import print_function
import contextlib


@contextlib.contextmanager
def debug(name):
    print("debugging %r:" % name)
    yield
    print("end of debugging %r" % name)


@debug("spam")
def spam():
    print("inside of spam function")


spam()
