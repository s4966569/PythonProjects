class ReplyItem:
    def __init__(self):
        self.author = None
        self.reply = None
        self.floor = None
        self.time = None

    def __str__(self):
        return self.author + "(" + self.floor + "," + self.time + ")" + "------" + self.reply

    def __repr__(self):
        return str(self)
