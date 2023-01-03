import pathlib

class Chip():
    def __init__(self, name, path_to_image, build_quality):
        self.name = name
        self.path = pathlib.Path(path_to_image)
        self.build_quality = build_quality
    
    def get_name(self):
        return self.name

    def rating(self):
        print("uh oh not implemented rating")
        raise NotImplementedError("Rating for chip not implemented")

class CPU(Chip):
    def __init__(self, name, path_to_image, build_quality, package, clockspeed):
        super().init(name, path_to_image, build_quality)
        self.package = package
        self.clockspeed = clockspeed