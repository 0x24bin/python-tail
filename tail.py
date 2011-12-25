#!/usr/bin/env python

'''
Python-Tail - Unix tail implementation in Python <https://github.com/kasun/python-tail>
Author - Kasun Herath <kasunh01 at gmail.com>
'''

import os
import time

class Tail:
    ''' Represent a tail command '''
    def __init__(self, file_):
        ''' Initiate a Tail instance '''
        self.check_file_validity(file_)
        self.tail_file = file_

    def follow(self, s=1):
        ''' Do tail follow '''
        if not self.callback:
            raise TailError('No callback function registered')
        file_ = open(self.tail_file)

        # Go to the end of file
        file_.seek(0,2)
        while 1:
            curr_position = file_.tell()
            line = file_.readline()
            if not line:
                file_.seek(curr_position)
            else:
                self.callback(line)
            time.sleep(s)
        file_.close()

    def register_callback(self, func):
        ''' Register a callback function to be called when a new line is found '''
        self.callback = func

    def check_file_validity(self, file_):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
