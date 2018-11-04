import os, sys, codecs, json, optparse

class INI():
    def __init__(self):
        self.ini_file_path = None
        self.json_file_path = None
        self.ini = {}
        self.ini_str = None
        self.ini_file_encode = "utf-8"
    
    def read_from_ini(self, file_path):
        """read ini string from *.ini file and convert to dict type object - self.ini

        args:
            file_path (str)
        """
        self.ini_file_path = file_path
        try:
            with codecs.open(self.ini_file_path, mode='r', encoding=self.ini_file_encode) as in_file:
                self.ini_str = filter(None, in_file.read().replace("\r", "").split("\n"))
        except Exception as e:
            print("[Error] EXCEPTION ON READING {}: {}".format(self.ini_file_path, str(e)))
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
        """read ini dict object from *.json file and update self.ini

        args:
            file_path (str)
        """
        self.json_file_path = file_path
        with open(self.json_file_path) as in_file:
            self.ini = json.load(in_file)

    def dump_to_ini(self, file_path=None):
        """convert and dump dict type object self.ini to *.ini file

        args:
            file_path (str)
        """
        write_path = self.ini_file_path
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
    
    def dump_to_json(self, file_path=None):
        """dump dict type object self.ini to *.json file

        args:
            file_path (str)
        """
        write_path = self.json_file_path
        if file_path:
            write_path = file_path
        with open(write_path, "w") as out_file:
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
