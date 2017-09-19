
class ReplyInfo:

    def __init__(self):
        self.author = None
        self.reply = None
        self.page = None
        self.floor = None
        self.time = None

    def __iter__(self):
        return iter([self.author, self.reply, self.page, self.floor, self.time])

    def __str__(self):
        return self.author + "(" + "第" + self.page + "页" + "," + self.floor + "," + str(self.time) + ")" + "------" + self.reply

    def __repr__(self):
        return str(self)
