#!/bin/python

from __future__ import print_function
import contextlib

@contextlib.contextmanager
def open_context_manager(filename, mode="r"):
    fh = open(filename, mode)
    yield fh
    fh.close()

with open_context_manager("contextlib_with1-1.txt", "w") as fh:
    print('The test 1 is complete!', file=fh); # uses __future__.print_function.print. see imports
    fh.write('The test 1 is complete!')

with contextlib.closing(open("contextlib_with1-2.txt", "w")) as fh:
    print('The test 2 is complete!', file=fh); # uses __future__.print_function.print. see imports
    fh.write('The test 2 is complete!');