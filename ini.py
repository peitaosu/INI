import os, sys, codecs

class INI():
    def __init__(self):
        self.file_path = None
        self.ini = {}
        self.ini_str = None
        self.ini_file_encode = "utf-8"
    
    def read_from_file(self, file_path):
        self.file_path = file_path
        with codecs.open(self.file_path, mode='r', encoding=self.ini_file_encode) as in_file:
            self.ini_str = filter(None, in_file.read().replace("\r", "").split("\n"))
        for ini_str in self.ini_str:
            if ini_str.startswith("#"):
                continue
            if ini_str.startswith("["):
                section = ini_str[1:-1]
                self.ini[section] = {}
                continue
            if "=" not in ini_str:
                continue
            self.ini[section][ini_str.split("=")[0]] = ini_str.split("=")[1]
    
    def write_to_file(self, file_path=None):
        write_path = self.file_path
        if file_path:
            write_path = file_path
        new_ini_str = []
        for section, keys in self.ini.iteritems():
            new_ini_str.append("[{}]".format(section))
            for key, value in keys.iteritems():
                try:
                    new_ini_str.append("{}={}".format(key, value))
                except Exception as e:
                    print("[Error] EXCEPTION ON {}: {}".format(key, str(e)))
        self.ini_str = new_ini_str
        with open(write_path, "w") as out_file:
            out_file.write("\n".join(self.ini_str))
