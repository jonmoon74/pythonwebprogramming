class Program():
    def __init__(self, *args, **kwargs):
        # __init__ method is to initialise the class - which sets defaults for the class
        self.lang = input("What language?: ")
        self.version = float(input("What version?: "))
        self.skill = input("What skill level?: ")
        # self allows reference from objects to the properties(e.g. p.lang)
        # *args - un-named arguments passed to function on calling
        # **kwargs - leyworded arguments passed to function on calling

    def upgrade(self):
        new_version = float(input("What version?: "))
        print("We have upgraded the version for", self.lang)
        self.version = new_version


p1 = Program()
