#dynamic typing

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")


class MyEditor:
     def execute(self):
        print("compiling")
        print("running")
        print("spell check")
        print("convention check")


class Laptop:
    def code(self,ide):
        ide.execute()

ide=PyCharm()  #type of ide is pycharm

lap1=Laptop()
lap1.code(ide)
