class Point:
    name =" "
    x = 0
    y = 0
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def fun(self):

        print("i am in fun in class Point")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def display(self):
        print("x is " + str(self.x) + "y is " + str(self.y))
        print("x is ", self.x, "y is ", self.y)


if __name__ == "__main__":
    print("Hello World")
    iamPoint = Point(6, 6)
    iamPoint.fun()
    iamPoint.move(9,2 )
    iamPoint.display()


