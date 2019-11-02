from datetime import datetime


class Recordfile:

    def __init__(self):
        self.file = open("tmp/record{0}.txt".format(datetime.now().strftime("%d%m%Y%H%M%S")), 'a')

    def write_record(self, record):
        self.file.write(record)

    def finish(self):
        self.file.close()
