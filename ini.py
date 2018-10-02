import os, sys

class INI():
    def __init__(self):
        self.file = None
        self.ini = None
    
    def read_from_file(self, file_path):
        self.file = file_path
        with open(file_path) as in_file:
            self.ini = in_file.readlines()