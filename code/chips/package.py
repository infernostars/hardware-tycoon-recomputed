import yaml
from pathlib import Path

class Package():
    def __init__(self, package_file):
        with open(Path(package_file), 'r') as file:
        self.dictionary = yaml.safe_load(file)