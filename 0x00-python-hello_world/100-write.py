#!/usr/bin/python3
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    exit(1)


eprint("and that piece of art is useful - Dora Korpar, 2015-10-19")
