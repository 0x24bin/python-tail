#!/usr/bin/env python

#
# Author - Kasun Herath <kasunh01 at gmail.com>
#

import os

class Tail:
    def __init__(self, *args):
        self.files = list(args)
        for file_ in self.files:
            if not os.access(file_, os.F_OK):
                raise TailError('file does not exist')
            if not os.access(file_, os.R_OK):
                raise TailError('file not readable')
            if os.path.isdir(file_):
                raise TailError('file is a directory')

    def add_files(self, *args):
        self.files.extend(list(args))
        print self.files

    def print_tail(self, *args, **kargs):
        pass

    def print_follow(self):
        pass

    def register_callback(self, func):
        self.callback = func

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
