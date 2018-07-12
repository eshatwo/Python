class MathDojo:

    def __init__(self):
        self.result = 0

    def a(self, *args):
        print(args)
        return self

    def add(self, *args):
        for i in args:
            self.result += i
        return self

    def subtract(self, *args):
        for i in args:
            self.result -= i
        return self

md = MathDojo()
print(md.add(2).add(2,5,1).subtract(3,2).result)