class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        message = "Start drawing"
        if self.title is not None:
            print(message, "with", self.title)
        else:
            print(message)


class Pen(Stationery):
    def draw(self):
        print("Start drawing with", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Start drawing with", self.title)


class Handle(Stationery):
    def draw(self):
        print("Start drawing with", self.title)


stationery = Stationery()
brush = Stationery("brush")
pen = Pen("pen")
pencil = Pencil("pencil")
handle = Handle("handle")

stationery.draw()
brush.draw()
pen.draw()
pencil.draw()
handle.draw()
