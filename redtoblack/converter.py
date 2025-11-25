# These imports are important here even if this module does not directly use them.
# The files being loaded contain references to objects from these modules and won't load
# if the modules haven't been imported.
import trinity
import audio2
import blue
import os

class RedToBlackConverter(object):
    def __init__(self):
        self.reader = blue.YamlReader()
        self.reader.doInitialize = False

        self.writer = blue.BlackWriter()

    def bake(self, file_path):
        obj = self.reader.CreateObjectFromFile(file_path)

        if not obj:
            raise ValueError("No binary object returned from parsing %s" % file_path)

        destination_path = os.path.splitext(file_path)[0] + ".black"
        self.writer.WriteObjectToFile(obj, destination_path)

        return destination_path