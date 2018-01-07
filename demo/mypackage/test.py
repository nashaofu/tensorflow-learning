class Test(object):
    length = 0
    def __init__(self, name='test'):
        self.name = name
        Test.length += 1

    def print(self):
        print(self.name)

    def getTestLength(self):
        return Test.length