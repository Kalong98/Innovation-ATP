class Clock:
    hour = 0
    minute = 0
    second = 0

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        s = "time: " + \
        "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute, self.second)
        print(s)

c1 = Clock(10, 25, 30)
c1.show()