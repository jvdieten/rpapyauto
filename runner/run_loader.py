class Runloader:

    def __init__(self, item):
        self.item = item
        self.actionlist = []

    def load_items(self):
        f = open(self.item, "r")
        lines = [line.rstrip('\r\n') for line in f]
        print('lines'+lines)
        self.actionlist = lines
