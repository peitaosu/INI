import os, sys

class INI():
    def __init__(self):
        self.file_path = None
        self.ini = None
    
    def read_from_file(self, file_path):
        self.file_path = file_path
        with open(self.file_path) as in_file:
            self.ini = in_file.readlines()
    
    def write_to_file(self, file_path=None):
        write_path = self.file_path
        if not file_path:
            write_path = file_path
        with open(write_path, "w") as out_file:
            out_file.write(self.ini)
    
    