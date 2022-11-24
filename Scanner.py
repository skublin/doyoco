import os
from glob import glob
from pathlib import Path
from Reporter import Reporter


class Scanner:
    def __init__(self, path):
        self.name = "Scanner"
        self.path = Path(path)
        self.structure = dict()
        self.indent = 0

    def generate_report(self):
        r = Reporter()
        if self.path.is_dir():
            print(f"{self.path} [root]")
            self.check_catalog(self.path)
    
    def check_catalog(self, catalog):
        self.indent += 2
        if catalog.is_dir():
            sub_directories = [x for x in catalog.iterdir() if x.is_dir()]
            files = [f for f in catalog.glob('*') if not os.path.isdir(f)]
            for d in sub_directories:
                print(f"{' ' * self.indent}-> {d} [directory]")
                self.check_catalog(d)
            for f in files:
                print(f"{' ' * self.indent}-> {f} [file]")
        self.indent -= 2
