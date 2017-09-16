class ReplyItem:
    def __init__(self):
        self.author = None
        self.reply = None
        self.floor = None
        self.time = None

    def __iter__(self):
        return iter([self.author, self.reply, self.floor, self.time])

    def __str__(self):
        return self.author + "(" + self.floor + "," + str(self.time) + ")" + "------" + self.reply

    def __repr__(self):
        return str(self)
