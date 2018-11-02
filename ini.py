import os, sys, codecs, json, optparse

class INI():
    def __init__(self):
        self.file_path = None
        self.ini = {}
        self.ini_str = None
        self.ini_file_encode = "utf-8"
    
    def read_from_ini(self, file_path):
        self.file_path = file_path
        try:
            with codecs.open(self.file_path, mode='r', encoding=self.ini_file_encode) as in_file:
                self.ini_str = filter(None, in_file.read().replace("\r", "").split("\n"))
        except Exception as e:
            print("[Error] EXCEPTION ON READING {}: {}".format(self.file_path, str(e)))
            return False
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
        return True
    
    def read_from_json(self, file_path):
        with open(file_path) as in_file:
            self.ini = json.load(in_file)

    def dump_to_ini(self, file_path=None):
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
    
    def dump_to_json(self, file_path):
        with open(file_path, "w") as out_file:
            json.dump(self.ini, out_file, indent=4)

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("--in_ini", dest="in_ini",
                      help="read from ini file")
    parser.add_option("--in_json", dest="in_json",
                      help="read from json file")
    parser.add_option("--out_ini", dest="out_ini",
                      help="dump to ini file")
    parser.add_option("--out_json", dest="out_json",
                      help="dump to json file")
    (options, args) = parser.parse_args()
    return options

if __name__=="__main__":
    opt = get_options()

    ini = INI()
    if opt.in_ini:
        ini.read_from_ini(opt.in_ini)
    if opt.in_json:
        ini.read_from_json(opt.in_json)

    if opt.out_ini:
        ini.dump_to_ini(opt.out_ini)
    if opt.out_json:
        ini.dump_to_json(opt.out_json)
