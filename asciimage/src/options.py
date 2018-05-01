class Options:
    def __init__(self, args):
        self.args = args

    def to_html(self):
        return self.args.s == True

    def to_grayscale(self):
        return self.args.g == True
